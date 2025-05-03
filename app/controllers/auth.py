from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fluxo_users = {
    "marcelo": {
        "username": "marcelo",
        "hashed_password": pwd_context.hash("marcelo123"),
    },
    "felipe": {
        "username": "felipe",
        "hashed_password": pwd_context.hash("felipe123"),
    },
    "rafael": {
        "username": "rafael",
        "hashed_password": pwd_context.hash("rafael123"),
    },
    "eymi": {
        "username": "eymi",
        "hashed_password": pwd_context.hash("eymi123"),
    },
}

SECRET_KEY = "chave_secreta_fluxo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_user(username: str):
    return fluxo_users.get(username)

def create_token(data: dict, expires: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    payload = data.copy()
    payload.update({"exp": datetime.utcnow() + expires})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form.username)
    if not user or not verify_password(form.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
    token = create_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(status_code=401)
    user = get_user(username)
    if user is None:
        raise HTTPException(status_code=401)
    return user