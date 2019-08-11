from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from FootballORM.db import Base

team_players = Table('team_players',
                     Base.metadata,
                     Column('team_id', Integer, ForeignKey('team.team_id')),
                     Column('player_id', Integer, ForeignKey('player.player_id'))
                     )


class Team(Base):
    __tablename__ = 'team'
    team_id = Column(Integer, primary_key=True)
    name = Column(String(45))
    players = relationship('Player',
                           secondary=team_players,
                           backref=backref('players'),
                           lazy='dynamic')


class Player(Base):
    __tablename__ = 'player'
    player_id = Column(Integer, primary_key=True)
    name = Column(String(45))
    playedfor = relationship('Team',
                             secondary=team_players,
                             backref=backref('team'),
                             lazy='dynamic')
