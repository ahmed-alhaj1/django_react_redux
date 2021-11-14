from django.apps import AppConfig
import pandas as pd

from joblib import load
import os


class MyAppConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    MLMODEL_FOLDER = os.path.join(BASE_DIR, 'my_app/mlmodel/')

    MLMODEL_FILE = os.path.join(MLMODEL_FOLDER, "IRISRandomForestClassifier.joblib")
    #mlmodel = load(MLMODEL_FILE)

