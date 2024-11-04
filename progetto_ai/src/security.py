# src/security.py

from cryptography.fernet import Fernet

# Usa una chiave fissa per la crittografia e decrittografia
key = b'6SBZk5X-AeY6IB4YmYPmP0rSuiZQ1pj1FwAuIqD1xoo='
cipher_suite = Fernet(key)

def encrypt_message(message: str, password: str) -> str:
    encrypted_text = cipher_suite.encrypt(message.encode())
    return encrypted_text.decode()

def decrypt_message(encrypted_message: str, password: str) -> str:
    decrypted_text = cipher_suite.decrypt(encrypted_message.encode())
    return decrypted_text.decode()
