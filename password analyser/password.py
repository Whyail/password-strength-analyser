import re

def is_strong_password(password):
    # Check minimum length
    if len(password) < 8:
        return False
    
    # Check if it contains both letters and digits
    if not (any(c.isalpha() for c in password) and any(c.isdigit() for c in password)):
        return False
    
    # Check if it contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

def main():
    
    password = input("Enter a password to analyze: ")
    
    if is_strong_password(password):
        print("Strong password!")
    else:
        print("Weak password. Please follow the password criteria.")
        

if __name__ == "__main__":
    main()


