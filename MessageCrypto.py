import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(password:str,salt:bytes) -> bytes:
    """ Kullanıcının parolasından, verilen salt ile anahtar üretir."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt = salt,
        iterations=390_000,
    )
    key = kdf.derive(password.encode("utf8"))
    return base64.urlsafe_b64encode(key)

def encrypt_with_password(password: str, plaintext: str) -> str:
    """
    plaintext'i password ile şifreler.
    Geriye 'salt:cipher' formatında bir string döner.
    """
    salt = os.urandom(16)  # Her seferinde yeni salt
    key = derive_key(password, salt)
    f = Fernet(key)
    token = f.encrypt(plaintext.encode("utf-8"))

    salt_b64 = base64.urlsafe_b64encode(salt).decode("utf-8")
    token_b64 = token.decode("utf-8")

    # Tek string içinde salt ve cipher'ı saklıyoruz
    return f"{salt_b64}:{token_b64}"

def decrypt_with_password(password: str, encrypted_block: str) -> str:
    """
    'salt:cipher' formatındaki metni, password ile çözer.
    Çözülen plain text'i string olarak döndürür.
    """
    salt_b64, token_b64 = encrypted_block.split(":", 1)

    salt = base64.urlsafe_b64decode(salt_b64.encode("utf-8"))
    token = token_b64.encode("utf-8")

    key = derive_key(password, salt)
    f = Fernet(key)

    plaintext = f.decrypt(token).decode("utf-8")
    return plaintext