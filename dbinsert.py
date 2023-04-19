from app import db
from app.models import User
 
db.create_all() # creates database

u = User(username='trungtran1234', email='trung.tran01@sjsu.com')
         
db.session.add(u) # similar to staging in git
db.session.commit()