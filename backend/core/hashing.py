# from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        # return pwd_context.verify(plain_password, hashed_password)
        return pbkdf2_sha256.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        # return pwd_context.hash(password)
        return pbkdf2_sha256.hash(password)
# h = Hasher()
# print(h.get_password_hash("supersecret1234"))