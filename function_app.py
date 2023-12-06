import azure.functions as func
from azure.functions import AuthLevel

import datetime
import json
import logging

from app.main import app as fastapi_app

app = func.AsgiFunctionApp(fastapi_app, http_auth_level=AuthLevel.ANONYMOUS)
