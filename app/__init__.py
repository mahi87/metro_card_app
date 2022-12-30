from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from celery import Celery


def make_celery(app):
    celery = Celery(app.import_name)
    celery.conf.update(app.config["CELERY_CONFIG"])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwds):
            with app.app_context():
                return self.run(*args, **kwds)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
celery = make_celery(app)


from app import routes, errors, models
