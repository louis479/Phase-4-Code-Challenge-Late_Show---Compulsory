from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .model import Episode, Guest, Appearance

__all__ = ["db", "Episode", "Guest", "Appearance"]

