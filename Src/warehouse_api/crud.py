from sqlalchemy.orm import Session
import models


def create_product(db: Session, product):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


def create_warehouse(db: Session, warehouse):
    db_warehouse = models.Warehouse(**warehouse.dict())
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse


def change_stock(db: Session, stock_data):
    stock = db.query(models.Stock).filter(
        models.Stock.product_id == stock_data.product_id,
        models.Stock.warehouse_id == stock_data.warehouse_id
    ).first()

    if stock:
        stock.quantity += stock_data.quantity
    else:
        stock = models.Stock(
            product_id=stock_data.product_id,
            warehouse_id=stock_data.warehouse_id,
            quantity=stock_data.quantity
        )
        db.add(stock)

    movement = models.Movement(
        product_id=stock_data.product_id,
        warehouse_id=stock_data.warehouse_id,
        change=stock_data.quantity
    )

    db.add(movement)
    db.commit()
    db.refresh(stock)
    return stock


def get_stocks(db: Session):
    return db.query(models.Stock).all()
