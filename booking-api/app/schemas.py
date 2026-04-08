"""Modelos Pydantic para validación de entrada/salida del booking-api."""

from datetime import date

from pydantic import BaseModel, Field


class BookingIn(BaseModel):
    guest: str = Field(..., min_length=1, max_length=100)
    room_type: str = Field(..., pattern="^(single|double|suite)$")
    check_in: date
    check_out: date


class BookingCreated(BaseModel):
    booking_id: str
    status: str


class BookingStatus(BaseModel):
    booking_id: str
    status: str
    last_update: str
    reason: str | None = None
