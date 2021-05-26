import datetime
import os


class Config:
    JWT_SECRET_KEY ='se'
    JWT_EXPIRATION_DELTA = datetime.timedelta(days=10)
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=10)

    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    DEBUG = True
    TESTING = True


class DevConfig(Config):
    DEBUG = True
    ENV = 'development'
    SECRET = "a"


class ProdConfig(Config):
    ENV = 'production'


config_options = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}
