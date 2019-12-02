from flask import Flask
from .app import app
from config.development import DevelopmentConfig
from config.staging import StagingConfig
from config.production import ProductionConfig

config_values = {
    "dev": DevelopmentConfig,
    "stg": StagingConfig,
    "prod": ProductionConfig,
}


def create_app(config_name='dev'):
    """
    Create App
    :param config_name:
    :return:
    """
    app_api = app
    load_config(app_api, config_name)

    return app_api


def load_config(app_config: Flask, config_mode) -> None:
    """
    Load the application's config
    :param (flask.app.Flask) app_config: The application instance Flask that'll be running
    :param config_mode: Config mode (Allowed: [dev, stg, prod])
    :return:
    """
    if config_mode in config_values:
        print("Config mode: {}".format(config_mode))
        app_config.config.from_object(config_values.get(config_mode))
    else:
        raise Exception("Configuration Mode Not Supported")
