import requests

from .constants import AIRPOL_URL

import json

from typing import Optional

from .apmodel import AirpolData

import os

API_KEY = os.getenv("API_KEY") or None

if not API_KEY:
    raise Exception("API_KEY doesn't exit")


def by_geoc(lat: float, lon: float, types: Optional[str] = "current") -> AirpolData:
    """
    Description
    -----------
    For Location coodinates returns:

    'AirpolData'

    Parameters
    ----------
    latitude : float
    longitude : float
    types : str, optional
        For value 'forecast' return forecast of next 5 days (default
        is current)

    Returns
    -------
    AirpolData
    """

    payload = {"lat": f"{lat}", "lon": f"{lon}", "appid": API_KEY}
    if types == "current":
        URL = f"{AIRPOL_URL}"
    elif types == "forecast":
        URL = f"{AIRPOL_URL}/{types.lower()}"
    else:
        raise Exception("types can either be current(default) or forecast")

    req = requests.get(URL, params=payload)
    if req.status_code==200:
        return AirpolData.parse_raw(json.dumps(req.json()))
    else:
        return req.json()
