from ninja import Schema
from typing import Optional
from datetime import datetime


class ClientOut(Schema):

    id: int
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    comment: Optional[str] = None
    addres: Optional[str] = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ClientIn(Schema):

    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
