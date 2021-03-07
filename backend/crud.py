from model import db, Facility


facility1 = Facility('リバーサイト', 1, '01', 'test')
facility2 = Facility('リバーサイト1', 2, '01', 'test')
facility3 = Facility('リバーサイト2', 3, '01', 'test')

# db.drop_all()
# db.create_all()

db.session.add_all([facility1, facility2])
db.session.add(facility3)

db.session.commit()
