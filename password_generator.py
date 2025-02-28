import secrets
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'

    print("\nGenerated Password:", generate_password(length, use_digits, use_specials))
