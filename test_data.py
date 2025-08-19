#This is where misc test data lives

#Invalid login credentials
INVALID_CREDS = {
    "blank_username": ("", "SomeValidPassword1!", {"username": "Please enter a valid email address."}),
    "invalid_username": ("invalidUser@authtest.com", "SomeValidPassword1!", {"message": "Incorrect Email or Password", "description": "Please try again or click Forgot Password to reset your password."}),
    "invalid_password": ("validUser@authtest.com", "wrongPass12345", {"message": "Incorrect Email or Password", "description": "Please try again or click Forgot Password to reset your password."}),
    "blank_password": ("validUser@authtest.com", "", {"password": "Please enter your password."}),
    "blank_both": ("", "", {"username": "Please enter a valid email address.", "password": "Please enter your password."}),
    "malformed_username": ("notAnEmail", "SomeValidPassword1!", {"username": "Please enter a valid email address."})
}
