import pandas as pd
from hopsworks_client import get_hopsworks_client
from features import preprocess 
import xgboost as xgb
import sklearn
import seaborn as sns
import joblib
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from hopsworks.hsfs.builtin_transformations import label_encoder
from config import IMAGES_DIR, MODELS_DIR, BASE_DIR
def main() -> None:
    print("Connecting to Hopsworks...")
    project = get_hopsworks_client()
    fs = project.get_feature_store()
    feature_group = fs.get_feature_group(name="titanic_features", version=1)
    print("Loading feature group...")
    selected_features = feature_group.select_features()
    feature_view = fs.get_or_create_feature_view(
        name="titanic_feature_view",
        version=1,
        description="Feature view for Titanic survival prediction",
        labels=["survived"],
        transformation_functions=[
                                 label_encoder("sex"),
                                 label_encoder("embarked")
                                 ],
        query=selected_features
    )
    print("Splitting train/test data...")
    X_train, X_test, y_train, y_test = feature_view.train_test_split(0.2)
   # Train the model
    print("Training model...")
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train.values.ravel())

    # Evaluate the model
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    metrics = classification_report(y_test, y_pred, output_dict=True)
    results = confusion_matrix(y_test, y_pred)

# Create the confusion matrix as a figure, we will later store it as a PNG image file
    print("Accuracy:", metrics["accuracy"])
    print("Weighted F1:", metrics["weighted avg"]["f1-score"])
    df_cm = pd.DataFrame(results, ['True Deceased', 'True Survivor'],
                     ['Pred Deceased', 'Pred Survivor'])
    cm = sns.heatmap(df_cm, annot=True)
    fig = cm.get_figure()

    model_dir = BASE_DIR / "titanic_model"
    images_dir = model_dir / "images"
    model_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    print("Saving local artifacts...")
    joblib.dump(model, model_dir / "titanic_model.pkl")
    fig.savefig(images_dir / "confusion_matrix.png")

    print("Registering model in Hopsworks...") 
    mr = project.get_model_registry()
    # Create an entry in the model registry that includes the model's name, desc, metrics
    titanic_model = mr.python.create_model(
    name="titanic", 
    metrics={"accuracy" : metrics['accuracy'], 
             'f1 score' : metrics['weighted avg']['f1-score']},
    feature_view=feature_view,
    description="Titanic Survivor Predictor"
    )
    titanic_model.save(str(model_dir))
    print("Training pipeline completed successfully.")

if __name__ == "__main__":
    main()