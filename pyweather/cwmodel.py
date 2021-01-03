from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import orjson


def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


class Coord(BaseModel):
    lon: float = Field(None, description="City geo location, longitude")
    lat: float = Field(None, description="City geo location, latitude")


class WeatherItem(BaseModel):
    id: int = Field(None, description="Weather condition id.")
    main: str = Field(
        None, description="Group of weather parameters (Rain, Snow, Extreme etc.)"
    )
    description: str = Field(None, description="Weather condition within the group.")
    icon: str = Field(None, description="Weather icon id.")


class Main(BaseModel):
    temp: float = Field(None, description="Temperature.")
    feels_like: float = Field(
        None,
        description="Temperature. This temperature parameter accounts for the human perception of weather.",
    )
    temp_min: float = Field(
        None,
        description="Minimum temperature at the moment. This is minimal currently observed temperature.",
    )
    temp_max: float = Field(
        None,
        description="Maximum temperature at the moment. This is maximal currently observed temperature.",
    )
    pressure: int = Field(
        None,
        description="Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa",
    )
    humidity: int = Field(None, description="Humidity, %")
    sea_level: Optional[int] = Field(
        None, description="Atmospheric pressure on the sea level, hPa"
    )
    grnd_level: Optional[int] = Field(
        None, description="Atmospheric pressure on the ground level, hPa"
    )


class Wind(BaseModel):
    speed: float = Field(None, description="Wind speed.")
    deg: int = Field(None, description="Wind direction, degrees (meteorological)")
    gust: Optional[int] = Field(None, description="Wind gust.")


class Clouds(BaseModel):
    all: int = Field(None, description="Cloudiness, %")


# class Rain(BaseModel):
#     1h: float = Field(None, description= 'Rain volume for the last 1 hour, mm')
#     3h: float = Field(None, description= 'Rain volume for the last 1 hour, mm')

# class Snow(BaseModel):
#     1h: float = Field(None, description= 'Snow volume for the last 1 hour, mm')
#     3h: float = Field(None, description= 'Snow volume for the last 3 hours, mm')


class Sys(BaseModel):
    type: int = Field(None, description="Internal parameter")
    id: int = Field(None, description="Internal parameter")
    message: float = Field(None, description="Internal parameter")
    country: str = Field(None, description="Country code (GB, JP etc.)")
    sunrise: int = Field(None, description="Sunrise time, unix, UTC ")
    sunset: int = Field(None, description="Sunset time, unix, UTC")


class WeatherData(BaseModel):
    coord: Coord
    weather: List[WeatherItem]
    base: str = Field(None, description="Internal parameter")
    main: Main
    visibility: int = Field(None, description="")
    wind: Wind
    clouds: Clouds
    # rain: Rain
    # snow: Snow
    dt: int = Field(None, description="Time of data calculation, unix, UTC")
    sys: Sys
    timezone: int = Field(None, description="Shift in seconds from UTC")
    id: int = Field(None, description="City ID")
    name: str = Field(None, description="City name")
    cod: int = Field(None, description="Internal parameter")

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
