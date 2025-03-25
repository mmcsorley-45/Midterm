"""Script to add users via terminal input and display all users."""

from app import create_app, db
from app.models.user import User

# Create Flask app context
app = create_app()

with app.app_context():
    name = input("Enter user's name: ")
    email = input("Enter user's email: ")

    if not name or not email:
        print("Name and email cannot be empty.")
    elif not email.lower().endswith("@kean.edu"):
        print("Invalid email. Must end with @school.edu.")
    else:
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        print(f"User {name} added with email {email}!")


    print("\nAll users in the database:")
    all_users = User.query.all()
    for user in all_users:
        print(f"- {user.name} ({user.email})")
