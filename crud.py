from sqlalchemy.orm import Session
import models , schemas

def get_item (db : Session , item_id : int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items (db : Session , skip : int = 0 , limit : int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item (db : Session , item : schemas.ItemCreate):
    db_item = models.Item ( brand = item.brand , color = item.color , price = item.price )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

def update_item (db : Session , item_id : int , item : schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if db_item is None :
        return None
    db_item.brand = item.brand
    db_item.color = item.color
    db_item.price = item.price

    db.commit()
    db.refresh(db_item)
    return db_item

def delets_item (db : Session , item_id = int) :
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item :
        db.delete(db_item)
        db.commit()
    return db_item