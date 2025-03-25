"""SQLAlchemy model for User."""

from app import db

# pylint: disable=too-few-public-methods
class User(db.Model):
    """Represents a user with name and email."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
