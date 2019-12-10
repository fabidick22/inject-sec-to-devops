from .default import Config


class DevelopmentConfig(Config):
    """
    Configurations for Development.
    """

    DEBUG = True
    TESTING = True
    SECRET = "DevelopSecret123!!"  # pragma: allowlist secret
