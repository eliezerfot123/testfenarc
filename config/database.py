from config.settings import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from environs import Env

env = Env()
env.read_env()
app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = env.str("DATABASE_URL")
db = SQLAlchemy(app)

db.create_all()
# migrate the database
Migrate(app, db)