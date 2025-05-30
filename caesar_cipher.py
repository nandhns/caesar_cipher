def encrypt(text: str, key: int) -> str:
    """
    Encrypts the given text using Caesar cipher with the specified key.
    
    Args:
        text (str): The plaintext to encrypt
        key (int): The shift value (can be positive or negative)
    
    Returns:
        str: The encrypted text
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Convert to 0-25 range, apply shift, and mod 26 to wrap around
            shifted = (ord(char) - ascii_base + key) % 26
            # Convert back to ASCII and append
            result += chr(shifted + ascii_base)
        else:
            # Preserve non-alphabetic characters
            result += char
    return result

def decrypt(ciphertext: str, key: int) -> str:
    """
    Decrypts the given ciphertext using Caesar cipher with the specified key.
    
    Args:
        ciphertext (str): The text to decrypt
        key (int): The shift value used for encryption
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with the negative key
    return encrypt(ciphertext, -key) 