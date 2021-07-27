
from ModelApp import db,teacher

 ### CREATE
firsteacher = teacher('itsaac',itsaac@gmail.com)
db.session.add(firsteacher)
firsteacher2 = teacher('itsaac2',itsaac@gmail.com)
db.session.add(firsteacher2)
db.session.commit()

## READ
all_firsteachers = teachers.query.all()
print(all_firsteachers)
print('\n')

# select by id
teacer_one = teachers.query.get(1)
print(teacer_one)
print(teacer_one.Email)
print('\n')
# Filters
teacer_sam = teachers.query.filter_by(name='itsaac')
print(teacer_sam)
print('\n')



## UPDATE
firsteacher = teacher.query.get(1)
firsteacher.age = 10
db.session.add(firsteacher)
db.session.commit()


## DELETE
secondteacher = teachers.query.get(2)
db.session.delete(secondteacher)
db.session.commit()


# Check it
allteachers = teachers.query.all()
print(allteachers)
