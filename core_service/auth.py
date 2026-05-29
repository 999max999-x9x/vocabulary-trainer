from jose import jwt
from datetime import datetime, timedelta


SECRET_KEY = "secret123"

ALGORITHM = "HS256"


def create_token(username):

    payload = {

        "sub": username,

        "exp": datetime.utcnow() + timedelta(hours=1)

    }

    token = jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM

    )

    return token