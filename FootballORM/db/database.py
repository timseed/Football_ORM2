from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session,scoped_session, sessionmaker
from sqlalchemy.ext.automap import automap_base


Base = automap_base()
engine = create_engine("sqlite:////Users/timothyhseed/PycharmProjects/Football_ORM/Football.db", echo=False)


def init_db():
    # Import the DB Models to be created.
    from FootballORM.model import my_model
    Base.prepare(engine, reflect=True)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)  # once engine is available
    session = Session()
    session.commit()


def use_db():
    # Import the DB Models to be created.
    from FootballORM.model import my_model
    Base.prepare(engine, reflect=True)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)  # once engine is available
    session = Session()
    return session


def delete_all(session):
    from FootballORM.model.my_model import Player,Team
    # Clearing all data
    session.query(Player).delete()
    session.query(Team).delete()
    # As this is not a Table in SqlAlchemy sense we can not delete it like this
    # session.query(team_players).delete()
    session.commit()
