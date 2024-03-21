def validate_user_data(logger, user_data):
    """
    Validates user data fetched from the API.
    Ensures that necessary fields are present and correctly formatted.

    :param user_data: dict representing a single user's data
    :return: True if valid, raises ValueError otherwise
    """
    required_fields = ["firstname", "lastname", "email"]

    if not all(field in user_data for field in required_fields):
        logger.error(
            f"Validation Error: Missing one of the required fields in {user_data}"
        )
        raise ValueError("Missing required user data fields.")

    if (
        not isinstance(user_data["firstname"], str)
        or not isinstance(user_data["lastname"], str)
        or not isinstance(user_data["email"], str)
    ):
        logger.error(
            f"Validation Error: One of the required fields is not a string in {user_data}"
        )
        raise ValueError("Invalid data type for one or more user fields.")

    # Further validation can be added here (e.g., regex for email)

    return True
