import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
LOGIN_URL = os.getenv("LOGIN_URL")
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
GRANT_TYPE = os.getenv("GRANT_TYPE")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
RESOURCE = os.getenv("RESOURCE")

# use above variables in our requests
response = requests.post(LOGIN_URL, data={
    'tenant_id': TENANT_ID,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': GRANT_TYPE,
    'resource': RESOURCE
}).json()

#print(response)
print(response['token_type'],response['access_token'])

# Create a function to retrieve access token

def get_access_token():
    return(response['token_type'],response['access_token'])
