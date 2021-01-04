import os

import json

import requests

from typing import Optional

from .constants import WEATH_URL

from .cwmodel import WeatherData

API_KEY = os.getenv("API_KEY") or None

if not API_KEY:
    raise Exception("API_KEY doesn't exit")


def by_cname(
    cityname: str,
    countrycode: Optional[str] = "",
    units: Optional[str] = "",
    lang: Optional[str] = "en",
) -> WeatherData.parse_raw:
    """
    Description
    -----------
    for a cityname, countrycode returns:

    'WeatherData'

    Parameters
    ----------
    cityname : str
        The name of the city or town
    countrycode : str, Optional
    units : str, Optional
        Temperature is available in Fahrenheit, Celsius and Kelvin units.
            For temperature in Fahrenheit use units=imperial
            For temperature in Celsius use units=metric
            Temperature in Kelvin is used by default
        Wind speed and gust is available in meter/sec, miles/hour.
            For meter/sec use units=metric
            For miles/hour use units=imperial
            meter/sec by default
    lang : str, Optional
        Language the information will be returned

    Returns
    -------
    WeatherData
    """
    payload = {
        "q": f"{cityname},{countrycode}",
        "units": f"{units}",
        "lang": f"{lang}",
        "appid": f"{API_KEY}",
    }
    req = requests.get(WEATH_URL, params=payload)
    if req.status_code==200:
        return WeatherData.parse_raw(json.dumps(req.json()))
    else:
        return req.json()


def by_cid(
    cityid: int, units: Optional[str] = "", lang: Optional[str] = "en"
) -> WeatherData.parse_raw:
    """
    Description
    -----------
    for a cityid returns:

    'WeatherData'

    Parameters
    ----------
    cityid : int
        The id of the city
    units : str, Optional
        Temperature is available in Fahrenheit, Celsius and Kelvin units.
            For temperature in Fahrenheit use units=imperial
            For temperature in Celsius use units=metric
            Temperature in Kelvin is used by default
        Wind speed and gust is available in meter/sec, miles/hour.
            For meter/sec use units=metric
            For miles/hour use units=imperial
            meter/sec by default
    lang : str, Optional
        Language the information will be returned

    Returns
    -------
    WeatherData
    """
    payload = {
        "id": f"{cityid}",
        "units": f"{units}",
        "lang": f"{lang}",
        "appid": f"{API_KEY}",
    }
    req = requests.get(WEATH_URL, params=payload)
    if req.status_code==200:
        return WeatherData.parse_raw(json.dumps(req.json()))
    else:
        return req.json()

def by_geoc(
    lat: float, lon: float, units: Optional[str] = "", lang: Optional[str] = "en"
) -> WeatherData.parse_raw:
    """
    Description
    -----------
    for a latitude, longitude returns:

    'WeatherData'

    Parameters
    ----------
    latitude : float
    longitude : float
    units : str, Optional
        Temperature is available in Fahrenheit, Celsius and Kelvin units.
            For temperature in Fahrenheit use units=imperial
            For temperature in Celsius use units=metric
            Temperature in Kelvin is used by default
        Wind speed and gust is available in meter/sec, miles/hour.
            For meter/sec use units=metric
            For miles/hour use units=imperial
            meter/sec by default
    lang : str, Optional
        Language the information will be returned

    Returns
    -------
    WeatherData
    """
    payload = {
        "lat": f"{lat}",
        "lon": f"{lon}",
        "units": f"{units}",
        "lang": f"{lang}",
        "appid": f"{API_KEY}",
    }
    req = requests.get(WEATH_URL, params=payload)
    if req.status_code==200:
        return WeatherData.parse_raw(json.dumps(req.json()))
    else:
        return req.json()
    
def by_zcode(
    zipcode: int,
    countrycode: str,
    units: Optional[str] = "",
    lang: Optional[str] = "en",
) -> WeatherData.parse_raw:
    """
    Description
    -----------
    for a zipcode, countrycode returns:

    'WeatherData'

    Parameters
    ----------
    zipcode : int
    countrycode : str
        The code of the country
    units : str, Optional
        Temperature is available in Fahrenheit, Celsius and Kelvin units.
            For temperature in Fahrenheit use units=imperial
            For temperature in Celsius use units=metric
            Temperature in Kelvin is used by default
        Wind speed and gust is available in meter/sec, miles/hour.
            For meter/sec use units=metric
            For miles/hour use units=imperial
            meter/sec by default
    lang : str, Optional
        Language the information will be returned

    Returns
    -------
    WeatherData
    """
    payload = {
        "zip": f"{zipcode},{countrycode}",
        "units": f"{units}",
        "lang": f"{lang}",
        "appid": f"{API_KEY}",
    }
    req = requests.get(WEATH_URL, params=payload)
    if req.status_code==200:
        return WeatherData.parse_raw(json.dumps(req.json()))
    else:
        return req.json()