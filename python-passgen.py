import random
import string


def generate_password(length: int = 10):
        # Variable parameter with default of 10
    alphabet = string.ascii_letters + string.digits + string.punctuation
        # Making a pool of 3 sets of strings
    password = ''.join(random.choice(alphabet) for i in range(length))  #
        # Randomly select x values from our alphabet
    return password


password = generate_password(20)
    # Output of our function; passing in a request for 20 characters
print(f"Generated Password: {password}")
