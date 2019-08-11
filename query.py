from FootballORM.db.database import use_db,engine, Base, delete_all
from FootballORM.model.my_model import Team,Player
from sqlalchemy import  select, text
session = use_db()

first_rec=session.query(Team).first()
print(f"Team: {first_rec.name}")
for n in first_rec.players:
    print(f"player: {n.name}")
print("*"*80)
#
# OK lets try and get Newcastle
#
nufc_recs=session.query(Team).filter(Team.name=="Newcastle").first()
print(f"Team: {nufc_recs.name}")
for n in nufc_recs.players:
    print(f"player: {n.name}")