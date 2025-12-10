from pydantic import BaseModel

class ItemBase (BaseModel):
    brand : str
    color : str
    price : float

class ItemCreate (ItemBase):
    pass

class ItemResponse (ItemBase):
    id : int

    class Config :
        orm_mode = True