from FootballORM.db.database import use_db,engine, Base, delete_all
from FootballORM.model.my_model import *
session = use_db()

#To see what tables we have
print(engine.table_names())
delete_all(session)

p1 = Player(name="Mo Salah")
p2 = Player(name="JoJo Shelvy")
p3 = Player(name="Dwight Gayle")
p4 = Player(name="Andy Carol")

session.add(p1)
session.add_all([p2,p3,p4])

t1 = Team(name="Liverpool")
session.add(t1)
t1.players.append(p1)
#
t2 = Team(name="Newcastle")
t2.players.append(p2)
t2.players.append(p3)
t2.players.append(p4)

session.commit()
