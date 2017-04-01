from sqlalchemy import create_engine, engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from sqlalchemy import Column, Integer, String, Float, JSON

engine = create_engine('mysql+mysqldb://trump:teretere11@konku.ccyfdsg989fi.eu-central-1.rds.amazonaws.com/trump',
                       convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)
    t = Tweet(1, 2, 3, 4, 5, 'et', '{}')
    db_session().add(t)


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True, autoincrement=False)
    reply_id = Column(Integer, nullable=True)
    vote = Column(Integer)
    sentiment = Column(Float, default=0)
    user_id = Column(Integer, nullable=False)
    country = Column(String(30), nullable=True)
    json = Column(JSON)

    def __init__(self, id=None, reply_id=None, vote=None, sentiment=None, user_id=None, country=None, json=None):
        self.id = id
        self.reply_id = reply_id
        self.vote = vote
        self.sentiment = sentiment
        self.user_id = user_id
        self.country = country
        self.json = json

