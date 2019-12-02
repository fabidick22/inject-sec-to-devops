from .default import Config


class ProductionConfig(Config):
    """
    Configurations for Production.
    """

    DEBUG = False
    TESTING = False
