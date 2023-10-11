from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from environs import Env
from flasgger import Swagger


env = Env()
env.read_env()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env.str("DATABASE_URL")

template = {
  "swagger": "2.0",
  "info": {
    "title": "MasLeads API",
    "description": "API for my data",
    "contact": {
      "responsibleOrganization": "ME",
      "responsibleDeveloper": "Me",
      "email": "eliezerjromeroc@gmail.com",
      "url": "linkedin.com/in/elioxrome/",
    },
    "termsOfService": "http://me.com/terms",
    "version": "0.0.1"
  },
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}

swagger = Swagger(app, template=template)

db = SQLAlchemy(app)