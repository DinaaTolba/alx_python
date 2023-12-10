def validate_password(password):
    if len(str(password)) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and not ' ' in password:
        return True
    else:
        return False
  
    