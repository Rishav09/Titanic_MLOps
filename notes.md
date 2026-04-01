Feature Group = data storage (table)
Feature View  = ML interface (query + transform)
Model Registry = model storage (versioned)

# Writing into feature Group Part
project = get_hopsworks_client()
fs = project.get_feature_store()

    feature_group = fs.get_or_create_feature_group(
        name="titanic_features",
        version=1,
        primary_key=["PassengerId"],
        event_time="event_time",
        description="Preprocessed features for Titanic survival prediction",
    )
    feature_group.insert(df, write_options={"wait_for_job": True})

## Reading from feature group as feature view Part

    feature_group = fs.get_feature_group(name="titanic_features", version=1)
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
