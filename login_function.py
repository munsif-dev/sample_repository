def login(username, password, user_db):
    """
    Simple login function.
    Args:
        username (str): The username to login.
        password (str): The password to login.
        user_db (dict): A dictionary with usernames as keys and passwords as values.
    Returns:
        bool: True if login is successful, False otherwise.
    """
    if username in user_db and user_db[username] == password:
        return True
    return False