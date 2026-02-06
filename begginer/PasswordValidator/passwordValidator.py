import re

def validate_password(password):
    error = []

    if len(password) < 8:
        error.append("Password must be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        error.append("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        error.append("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):   
        error.append("Password must contain at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        error.append("Password must contain at least one special character.")  
    
    return error

while True:
    password = input("Enter a password to validate: ")
    error = validate_password(password)

    if not error:
        print("Password is valid!")
        break

    else:
        print("Password is invalid:")
        for e in error:
            print(f"- {e}")
        print("Please try again.\n")