import requests
from sqlalchemy.exc import SQLAlchemyError
from models import Session, User
from utils import validate_user_data


def fetch_users(logger):
    try:
        response = requests.get("https://fakerapi.it/api/v1/users?_quantity=5")
        response.raise_for_status()  # Raises an HTTPError if the response is 4XX or 5XX
        users_data = response.json().get("data", [])

        if not isinstance(users_data, list):
            raise ValueError("Invalid data format received from API")

        return users_data
    except requests.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except ValueError as val_err:
        logger.error(f"Value error: {val_err}")


def store_users(users_data, logger):
    try:
        with Session() as session:
            for user_data in users_data:
                if validate_user_data(logger, user_data):
                    user = User(
                        name=f"{user_data['firstname']} {user_data['lastname']}",
                        email=user_data["email"],
                    )
                    session.add(user)
            session.commit()
        logger.info("Users fetched and stored successfully.")
    except SQLAlchemyError as db_err:
        logger.error(f"Database error occurred: {db_err}")
