from sqlalchemy import Column, Integer, String , Float
from database import Base

class Item(Base):
    __tablename__ = "item" 
    
    id    = Column (Integer , primary_key=True , index= True)
    brand = Column (String , index=True)
    color = Column (String , index= True)
    price = Column (Float , index=0)