import json
from google.cloud import datastore
from google.oauth2 import service_account
from app.models.base import settings

if settings.STAGE == "dev":
    credentials = service_account.Credentials.from_service_account_info(json.loads(settings.KEY_JSON_DATA))
    db_client = datastore.Client(credentials=credentials)
else:
    db_client = datastore.Client()
