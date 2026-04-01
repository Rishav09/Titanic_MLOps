import hopsworks
from config import settings 

def get_hopsworks_client():
    """
    Initializes and returns a Hopsworks client using the API key from the environment variables.
    
    Returns:
        hopsworks.client: An instance of the Hopsworks client.
    """
    try:
        # Initialize the Hopsworks client
        client = hopsworks.login(
            api_key_value=settings.HOPSWORKS_API_KEY, project="Titanic_Survival"
        )
        return client
    except Exception as e:
        print(f"Error initializing Hopsworks client: {e}")
        raise