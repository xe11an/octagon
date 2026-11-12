from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

# --- Схемы для Категорий ---
class CategoryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Название категории")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Название книги")
    description: Optional[str] = Field(None, max_length=2000, description="Описание")
    # gt=0 для цены больше 0
    price: float = Field(..., gt=0, description="Цена книги (должна быть больше 0)")
    url: Optional[str] = Field(None, description="Ссылка на товар")
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    price: Optional[float] = Field(None, gt=0)
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)