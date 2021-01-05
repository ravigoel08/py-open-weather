<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="assets/Samarkan.png" width="800" />
  
  <h3 align="center">py-open-weather</h3>
  
  <p align="center">
    A python3 library providing information of Current & Forecast of Weather as well as Air Pollution based on data from OpenWeatherMap.
    <br />
    <a href="https://github.com/ravigoel08/py-open-weather"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ravigoel08/py-open-weather/blob/master/assets/">View Demo</a>
    ·
    <a href="https://github.com/ravigoel08/py-open-weather/issues">Report Bug</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-package">About The Library</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Library


A python3 library providing information of Current & Forecast of Weather as well as Air Pollution based on data from OpenWeatherMap.

### Built With 

* [Requests](https://requests.readthedocs.io/en/master/)
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [orjson](https://pypi.org/project/orjson/)
* [Python3](https://www.python.org/) :snake:



<!-- GETTING STARTED -->
## Getting Started 


### Prerequisites 

Python3 and Above

### Installation 

1. Install the Library :eyes:
   ```sh
   pip install py-open-weather
   ```
![demo1](assets/demo1.gif)

2. And you are done :boom:



<!-- USAGE EXAMPLES -->
## Usage 
* (Current) Air pollution Data based on longitude and latitude 

```sh
>>> from pyweather import airpol
>>> airpol.by_geoc(50,50)
```
![demo2](assets/demo2.gif)

* (Forecast) Air pollution Data based on longitude and latitude 
```sh
>>> from pyweather import airpol
>>> airpol.by_geoc(50,50,'forecast')
```

* Current Weather Data based on cityname
```sh
>>> from pyweather import curweath
>>> curweath.by_cname('delhi')
```
![demo3](assets/demo3.gif)

* Current Weather Data based on city id
```sh
>>> from pyweather import curweath
>>> curweath.by_cid(2172797)
```
![demo4](assets/demo4.gif)

* Current Weather Data based on zipcode and country code
```sh
>>> from pyweather import curweath
>>> curweath.by_zcode(110032, 'in')
```
![demo5](assets/demo5.gif)

* Current Weather Data based on Longitude and Latitude
```sh
>>> from pyweather import curweath
>>> curweath.by_geoc(50,50)
```
![demo6](assets/demo6.gif)




<!-- LICENSE -->
## License 

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

CodewithRv - ravigoel.1997@gmail.com

Project Link: [https://github.com/ravigoel08/py-open-weather](https://github.com/ravigoel08/py-open-weather)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[contributors-url]: https://github.com/ravigoel08/py-open-weather/graphs/contributors
[forks-url]: https://github.com/ravigoel08/py-open-weather/network/members
[stars-url]: https://github.com/ravigoel08/py-open-weather/stargazers
[issues-url]: https://github.com/ravigoel08/py-open-weather/issues
[linkedin-url]: https://www.linkedin.com/in/ravi-goyal52/
[contributors-shield]: https://img.shields.io/github/contributors/ravigoel08/py-open-weather?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/ravigoel08/py-open-weather?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/ravigoel08/py-open-weather?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/ravigoel08/py-open-weather?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
