from config.settings import app, db
from flask_migrate import Migrate
from apps.process.views import process_app

app_main = app
Migrate(app_main, db)
app.register_blueprint(process_app)

if __name__ == '__main__':
    app_main.run()