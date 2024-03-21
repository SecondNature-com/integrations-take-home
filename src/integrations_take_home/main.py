import logging

from models import init_db
from fetch_and_store import store_users, fetch_users

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting integrations_take_home")
    # Initialize the database and tables
    init_db(logger)
    # Fetch data from the API
    user_data = fetch_users(logger)
    # store it in the database
    store_users(user_data, logger)


if __name__ == "__main__":
    main()
