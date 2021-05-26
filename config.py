class Config:
    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    DEBUG = True
    TESTING = True


class DevConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProdConfig(Config):
    ENV = 'production'


config_options = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}
