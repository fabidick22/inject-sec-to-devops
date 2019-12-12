from .default import Config


class DevelopmentConfig(Config):
    """
    Configurations for Development.
    """

    DEBUG = True
    TESTING = True