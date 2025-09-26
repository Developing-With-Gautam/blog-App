from passlib.context import CryptContext

pass_crypt = CryptContext(schemes=['sha256_crypt'],deprecated = "auto")
class Hash():
    def hash_password(password:str):
        return pass_crypt.hash(password)

        