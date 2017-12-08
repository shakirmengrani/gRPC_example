from sqlalchemy import *
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("sqlite:///memory.db")
base = declarative_base()

class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (self.name, self.email)

class Address(base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Address(user_id='%s', location='%s')>" % (self.user_id, self.location)

User.addresses = relationship("Address", back_populates = "users")
Address.users = relationship("User", back_populates = "addresses")
base.metadata.create_all(engine)
sess = sessionmaker(bind=engine)
db = sess()
#     user_1 = User(name="Shakir Mengrani", email="shakircommando@gmail.com")
#     db.add(user_1)
#     user_2 = User(name="Shakir Mengrani1", email="shakircommando@gmail.com")
#     db.add(user_2)
#     db.commit()
#     address_1_user_1 = Address(location="Karachi, Pakistan", user_id=user_1.id)
#     db.add(address_1_user_1)
#     address_1_user_2 = Address(location="Karachi, Pakistan", user_id=user_2.id)
#     db.add(address_1_user_2)
#     db.commit()