"""Entry point for our twitoff flask app"""

# try to have minimal amount of code
from .app import create_app

APP = create_app()
