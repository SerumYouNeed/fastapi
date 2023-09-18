from passlib.context import CryptContext

# To mówi jakiego algo chcę użyć do hashowania haseł
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Ta funkcja zahaszuje hasło w bazie danych
def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)