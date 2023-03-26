import os
from google.cloud import datastore
from google.oauth2 import service_account
from app.models.base import Settings


credentials = service_account.Credentials.from_service_account_info(Settings.key_json_data)
db_client = datastore.Client(credentials=credentials)

