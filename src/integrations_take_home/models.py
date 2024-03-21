from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine("sqlite:///../../take_home.db")
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


def init_db(logger):
    try:
        logger.info("Initializing database")
        Base.metadata.create_all(engine)
    except Exception as e:
        logger.error(f"Error initializing db: {e}")
