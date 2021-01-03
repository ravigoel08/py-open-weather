from __future__ import annotations

from typing import List, Dict

from pydantic import BaseModel, Field

import orjson


def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


class Main(BaseModel):
    aqi: int = Field(
        None,
        description="Air Quality Index Possible values: 1, 2, 3, 4, 5. Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor.",
    )


class Components(BaseModel):
    co: float = Field(None, description="Сoncentration of CO (Carbon monoxide), μg/m3")
    no: float = Field(
        None, description="Сoncentration of NO (Nitrogen monoxide), μg/m3"
    )
    no2: float = Field(
        None, description="Сoncentration of NO2 (Nitrogen dioxide), μg/m3"
    )
    o3: float = Field(None, description="Сoncentration of O3 (Ozone), μg/m3")
    so2: float = Field(
        None, description="Сoncentration of SO2 (Sulphur dioxide), μg/m3"
    )
    pm2_5: float = Field(
        None, description="Сoncentration of PM2.5 (Fine particles matter), μg/m3"
    )
    pm10: float = Field(
        None, description="Сoncentration of PM10 (Coarse particulate matter), μg/m3"
    )
    nh3: float = Field(None, description="Сoncentration of NH3 (Ammonia), μg/m3")


class ListItem(BaseModel):
    dt: int = Field(None, description="Date and time, Unix, UTC")
    main: Main
    components: Components


class AirpolData(BaseModel):
    coord: Dict[str, float] = Field(
        None,
        description="Coordinates from the specified location (latitude, longitude)",
    )
    list: List[ListItem]

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
