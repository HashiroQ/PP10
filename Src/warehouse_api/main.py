from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import engine, get_db, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Warehouse Management API")


@app.get("/")
def root():
    return {"message": "Warehouse API is running"}


@app.post("/products/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@app.get("/products/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@app.post("/warehouses/", response_model=schemas.WarehouseResponse)
def create_warehouse(warehouse: schemas.WarehouseCreate, db: Session = Depends(get_db)):
    return crud.create_warehouse(db, warehouse)


@app.post("/stocks/change", response_model=schemas.StockResponse)
def change_stock(stock: schemas.StockChange, db: Session = Depends(get_db)):
    return crud.change_stock(db, stock)


@app.get("/stocks/", response_model=list[schemas.StockResponse])
def get_stocks(db: Session = Depends(get_db)):
    return crud.get_stocks(db)
