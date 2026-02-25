from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    sku: str


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True


class WarehouseCreate(BaseModel):
    name: str
    location: str


class WarehouseResponse(WarehouseCreate):
    id: int

    class Config:
        from_attributes = True


class StockChange(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int


class StockResponse(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int

    class Config:
        from_attributes = True
