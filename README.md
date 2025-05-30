# Caesar Cipher Implementation

This module provides a simple implementation of the Caesar cipher, a classical substitution cipher that shifts letters in the alphabet by a fixed number of positions.

## Features

- Encryption and decryption functions
- Preserves case (uppercase/lowercase)
- Preserves non-alphabetic characters (spaces, punctuation, numbers)
- Handles positive and negative shift keys
- Includes comprehensive unit tests

## Usage

```python
from caesar_cipher import encrypt, decrypt

# Encryption
plaintext = "Hello, World!"
key = 3
encrypted = encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")  # Output: "Khoor, Zruog!"

# Decryption
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")  # Output: "Hello, World!"
```

## Functions

### encrypt(text: str, key: int) -> str

Encrypts the given text using the Caesar cipher with the specified key.

- `text`: The plaintext to encrypt
- `key`: The shift value (can be positive or negative)
- Returns: The encrypted text

### decrypt(ciphertext: str, key: int) -> str

Decrypts the given ciphertext using the Caesar cipher with the specified key.

- `ciphertext`: The text to decrypt
- `key`: The shift value used for encryption
- Returns: The decrypted text

## Testing

Run the unit tests using:

```bash
python -m unittest test_caesar_cipher.py
```

## Implementation Details

- The cipher preserves the case of letters (uppercase/lowercase)
- Non-alphabetic characters are preserved without modification
- The key can be any integer (positive or negative)
- Keys larger than 26 or smaller than -26 are automatically wrapped around using modulo operation 