from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.dialects.postgresql
import os
from dotenv import load_dotenv
load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DATABASE')
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

class SingletonSQLAlchemyClient:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            print(POSTGRES_URL)
            engine = create_engine(POSTGRES_URL)
            Session = sessionmaker(bind=engine)
            cls.__instance.session = Session()
        return cls.__instance

client = SingletonSQLAlchemyClient()