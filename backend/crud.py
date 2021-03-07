from model import db, Facility

db.create_all()

facility1 = Facility('リバーサイト', 1, '01', 'test')
facility2 = Facility('リバーサイト1', 2, '01', 'test')
facility3 = Facility('リバーサイト2', 3, '01', 'test')

db.session.add_all([facility1, facility2])
db.session.add(facility3)

db.session.commit()