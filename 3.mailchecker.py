import re

def is_valid_email(email):
    # Regular expression pattern for basic email validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

while True:
    user_input = input("Enter an email address: ")
    
    if is_valid_email(user_input):
        print("Valid email:", user_input)
        break
    else:
        print("Invalid email. Please try again.")
