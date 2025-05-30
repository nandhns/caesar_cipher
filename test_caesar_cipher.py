import unittest
from caesar_cipher import encrypt, decrypt

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_basic(self):
        """Test basic encryption with a positive key"""
        self.assertEqual(encrypt("hello", 3), "khoor")
        self.assertEqual(encrypt("HELLO", 3), "KHOOR")
        self.assertEqual(encrypt("Hello World", 3), "Khoor Zruog")

    def test_decrypt_basic(self):
        """Test basic decryption with a positive key"""
        self.assertEqual(decrypt("khoor", 3), "hello")
        self.assertEqual(decrypt("KHOOR", 3), "HELLO")
        self.assertEqual(decrypt("Khoor Zruog", 3), "Hello World")

    def test_preserve_non_alpha(self):
        """Test preservation of non-alphabetic characters"""
        text = "Hello, World! 123"
        key = 3
        encrypted = encrypt(text, key)
        self.assertEqual(encrypted, "Khoor, Zruog! 123")
        self.assertEqual(decrypt(encrypted, key), text)

    def test_wrap_around(self):
        """Test wrapping around the alphabet"""
        self.assertEqual(encrypt("xyz", 3), "abc")
        self.assertEqual(encrypt("XYZ", 3), "ABC")
        self.assertEqual(decrypt("abc", 3), "xyz")
        self.assertEqual(decrypt("ABC", 3), "XYZ")

    def test_negative_key(self):
        """Test encryption and decryption with negative keys"""
        self.assertEqual(encrypt("def", -3), "abc")
        self.assertEqual(decrypt("abc", -3), "def")

    def test_large_key(self):
        """Test with keys larger than 26"""
        self.assertEqual(encrypt("hello", 29), "khoor")  # 29 % 26 = 3
        self.assertEqual(decrypt("khoor", 29), "hello")

if __name__ == '__main__':
    unittest.main() 