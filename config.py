import os

basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you_will_never_guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CELERY_CONFIG = {
        "broker_url": "redis://localhost:6379",
        "result_backend": "redis://localhost:6379",
    }
