from hopsworks_client import get_hopsworks_client
import joblib

def main() -> None:
    # -------------------------
    # Connect
    # -------------------------
    project = get_hopsworks_client()
    fs = project.get_feature_store()
    mr = project.get_model_registry()

    # -------------------------
    # Load model + feature view
    # -------------------------
    model_reg = mr.get_model("titanic", version=1)
    feature_view = model_reg.get_feature_view()

    # -------------------------
    # Download model
    # -------------------------
    model_dir = model_reg.download()
    print("Model downloaded to:", model_dir)
    model = joblib.load(model_dir + "/titanic_model.pkl")

    # -------------------------
    # Get batch data
    # -------------------------
    feature_view.init_batch_scoring(training_dataset_version=1)
    batch_data = feature_view.get_batch_data()

    # -------------------------
    # Predict
    # -------------------------
    preds = model.predict(batch_data)

    # -------------------------
    # Output latest prediction
    # -------------------------
    print("Latest prediction:", preds[-1])


if __name__ == "__main__":
    main()