from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)
pjt_dir = os.getcwd()
app.config.from_pyfile(f'{pjt_dir}/main/default.cfg')