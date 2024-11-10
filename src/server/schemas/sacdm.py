from pydantic import BaseModel
from typing import Optional


class SACDMSchema(BaseModel):
    device_id: int
    x_value: float
    y_value: float
    z_value: float
    timestamp: str
    label: str
    vehicle_id: Optional[int]