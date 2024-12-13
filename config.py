from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class DBSettings():
    @staticmethod
    def get_session():
        engine = create_engine("postgresql+psycopg2://postgres:mumano678@localhost:5432/System_PZ_10")
        return Session(bind=engine)