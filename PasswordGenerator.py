import random
import string

# Set of confusing characters to optionally exclude
similar_chars = {'l', 'I', '1', 'O', '0'}

# Syllables for pronounceable passwords
syllables = ['ba', 'be', 'bi', 'bo', 'bu', 'ka', 'ke', 'ki', 'ko', 'ku',
             'ma', 'me', 'mi', 'mo', 'mu', 'ra', 're', 'ri', 'ro', 'ru',
             'ta', 'te', 'ti', 'to', 'tu', 'na', 'ne', 'ni', 'no', 'nu']
 
def generate_password(min_length, numbers=True, special_characters=True,
                      avoid_similar=True, pronounceable=False):
    
    if pronounceable:
        password = ''
        while len(password) < min_length:
            password += random.choice(syllables)
        password = password[:min_length]
        # Insert at least one digit if requested
        if numbers:
            digit = random.choice(string.digits)
            idx = random.randint(0, len(password))
            password = password[:idx] + digit + password[idx:]
        # Insert at least one special character if requested
        if special_characters:
            special = string.punctuation
            special_char = random.choice(special)
            idx = random.randint(0, len(password))
            password = password[:idx] + special_char + password[idx:]
        # Trim to min_length + up to 2 if both number and special requested
        return password[:min_length + numbers + special_characters]

    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    if avoid_similar:
        letters = ''.join([ch for ch in letters if ch not in similar_chars])
        digits = ''.join([ch for ch in digits if ch not in similar_chars])
        # ❗ Don't filter special characters — most are safe and not confusing
        # special = ''.join([ch for ch in special if ch not in similar_chars])

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password_chars = []

    # ✅ Ensure at least one digit and one special character (if requested)
    if numbers:
        password_chars.append(random.choice(digits))
    if special_characters:
        password_chars.append(random.choice(special))

    # Fill remaining characters
    while len(password_chars) < min_length:
        password_chars.append(random.choice(characters))

    random.shuffle(password_chars)
    return ''.join(password_chars)

# -------------------- USER INPUTS --------------------
min_length = int(input("Enter minimum password length: "))
has_numbers = input("Should it contain numbers? (yes/no): ").strip().lower() == 'yes'
has_special = input("Should it contain special characters? (yes/no): ").strip().lower() == 'yes'
avoid_similar = input("Avoid similar confusing characters (like 1, l, 0, O)? (yes/no): ").strip().lower() == 'yes'
use_pronounceable = input("Make it pronounceable (easy to remember)? (yes/no): ").strip().lower() == 'yes'

# Generate password
pwd = generate_password(min_length, has_numbers, has_special, avoid_similar, use_pronounceable)
print("\n🔐 Your generated password is:", pwd)

# Optional save
save = input("\nDo you want to save this password to a file? (yes/no): ").strip().lower() == 'yes'
if save:
    filename = input("Enter file name (e.g., my_password.txt): ").strip()
    with open(filename, 'w') as f:
        f.write(f"Generated Password: {pwd}\n")
    print(f"✅ Password saved to '{filename}'")
