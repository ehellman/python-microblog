from flask import Flask

# create the application object (of class Flask)
app = Flask(__name__)
app.config.from_object('config')
# import the views module
from app import views
