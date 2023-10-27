import os
from dotenv import load_dotenv


site_root = os.path.dirname(os.getcwd())
dev_env_file = site_root + "/api/dev.env"
env_file = site_root + "/api/.env"


class Config:
    DEBUG = False


if os.path.exists(dev_env_file):
    load_dotenv(dev_env_file)

    class EnvConfig(Config):
        DEBUG = bool(os.environ.get("DEBUG"))
        MONGODB_HOST = os.environ.get("MONGODB_HOST")
        MONGODB_PORT = int(os.environ.get("MONGODB_PORT"))
        MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
        MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")


else:
    load_dotenv(env_file)

    class EnvConfig(Config):
        pass
