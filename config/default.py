import os


class Config:
    """
    Parent configuration class.
    """

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

    TITLE = "Test API"
    VERSION = "1.0"
    DESCRIPTION = "Demo API."
