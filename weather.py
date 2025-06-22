import os
import requests
from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user

router = APIRouter()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@router.get("/weather")
def get_weather(city: str, user=Depends(get_current_user)):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    if res.status_code != 200:
        raise HTTPException(status_code=400, detail="City not found")
    data = res.json()
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }