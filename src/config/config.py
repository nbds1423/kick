from dotenv import load_dotenv
from typing import Dict
import os
load_dotenv(dotenv_path='./.env')

def env() -> Dict[str, str]:

    cookie = os.getenv("COOKIE")
    token = os.getenv("TOKEN")
    database = os.getenv("DATABASE")

    envError(cookie, token, database)

    return {
        "cookie": cookie,
        "token": token,
        "database": database,
    }

def envError(cookie, token, database) -> None:
    if cookie is None or len(cookie) <= 0:
        raise Exception('Cookie missing in .env file.')
    elif token is None or len(token) <= 0:
        raise Exception('Token missing in .env file.')
    elif database is None or len(database) <= 0:
        raise Exception('Database URL missing in .env file.')
