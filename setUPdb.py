
from ModelApp import db,teacher

# Create
db.create_all()

# Create new row  in database
avi = teacher('avi','avi@gmail')
moti = teacher('moti','moti@gmail')

# Check ids
print(avi.id)
print(moti.id)
# or
db.session.add_all([avi,moti])
#the id creat auto

# Aanother option
# db.session.add(avi)
# db.session.add(moti)

# save it on db
db.session.commit()
print(avi.id)
print(moti.id)
