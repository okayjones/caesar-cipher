import string
import nltk
from nltk.corpus import words
nltk.download('words', quiet=True)

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
WORDS = words.words()

def encrypt(plain, key):
    encrypted = ''
    for c in plain:
        if c.isalpha():
            alpha = LOWER if c.islower() else UPPER
            encrypted += alpha[(alpha.index(c) + key) % 25]
        else:
            encrypted += c
    return encrypted

def decrypt(encrypted, key):
    return encrypt(encrypted, -key)

def crack(encrypted):
    attempts = {}
    for key in range(26):
        decrypted = decrypt(encrypted, key)
        decrypted_words = decrypted.split()
        matches = sum([1 for w in decrypted_words if w in WORDS])
        attempts[decrypted] = matches
    best_match = max(attempts, key=attempts.get)
    return best_match

