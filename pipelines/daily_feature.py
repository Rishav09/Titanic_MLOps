from hopsworks_client import get_hopsworks_client
from hopsworks_client import get_hopsworks_client
from generate_data import generate_random_passenger
from features import preprocess 
import time



def main() -> None:
    print("Connecting to Hopsworks...")
    project = get_hopsworks_client()
    fs = project.get_feature_store()

    print("Loading feature group...")
    fg = fs.get_feature_group(name="titanic_features", version=1)

    # Avoid full fg.read() just to get max id
    next_id = int(time.time())

    print("Generating new passenger...")
    new_df = generate_random_passenger(next_id)

    print("Preprocessing passenger...")
    new_df = preprocess(new_df)

    print("Inserting row into feature group...")
    fg.insert(new_df, write_options={"wait_for_job": True})

    print("Daily feature pipeline completed.")
    print(new_df)


if __name__ == "__main__":
    main()