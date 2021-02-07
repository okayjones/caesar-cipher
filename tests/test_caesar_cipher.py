import random
import pytest
from caesar_cipher import __version__
from caesar_cipher.cipher import encrypt, decrypt, crack

def test_caesar_cipher_encrypt():
    actual = encrypt('AbC dEf!', 27)
    expected = 'BcD eFg!'
    assert actual == expected

def test_caesar_cipher_decrypt():
    actual = decrypt('BcD eFg!', 27)
    expected = 'AbC dEf!'
    assert actual == expected

def test_caesar_cipher_crack(dickens):
    key = random.randint(1,27)
    encrypted = encrypt(dickens, key)
    actual = crack(encrypted)
    expected = dickens

@pytest.fixture
def dickens():
    return "It was the best of times, it was the worst of times."
