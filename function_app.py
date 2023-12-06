import azure.functions as func

import datetime
import json
import logging

from app.main import app as fastapi_app

app = func.AsgiFunctionApp(fastapi_app)
