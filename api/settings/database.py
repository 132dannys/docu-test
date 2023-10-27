from mongoengine import connect

from settings.config import EnvConfig


connect(host=EnvConfig.MONGODB_HOST, port=EnvConfig.MONGODB_PORT, username=EnvConfig.MONGODB_USERNAME,
        password=EnvConfig.MONGODB_PASSWORD, authSource="admin")
