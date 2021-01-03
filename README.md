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
  <h3 align="center">PYZIPCIN</h3>

  <p align="center">
    A python3 library providing information and validation of ZIP codes of India based on data from data.gov.in(2019)
    <br />
    <a href="https://github.com/ravigoel08/pyzipcin"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ravigoel08/pyzipcin/blob/master/assets/demo1.gif">View Demo</a>
    ·
    <a href="https://github.com/ravigoel08/pyzipcin/issues">Report Bug</a>
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


A python3 library providing information of ZIP codes of India as well as Verify Pincode based on data from data.gov.in(2019)

### Built With 

* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Python3](https://www.python.org/) :snake:



<!-- GETTING STARTED -->
## Getting Started 


### Prerequisites 

Python3 and Above

### Installation 

1. Install the Library :eyes:
   ```sh
   pip install pyzipcin
   ```

2. And you are done :boom:



<!-- USAGE EXAMPLES -->
## Usage 

```sh
>>> from pyzipcin import *

>>> decode(110032)     # decode(pincode, all_result=False)
>>> [{'circlename': 'Delhi Circle', 'regionname': 'NA', 'divisionname': 'Delhi East Division', 'officename': 'Babarpur SO North East Delhi', 'pincode': 110032, 'officetype': 'SO', 'delivery': 'Non Delivery', 'district': 'SHAHDARA', 'statename': 'Delhi'}]

>>> encode('kullu')    # encode(districtname)
>>> [{'pincode': 175101, 'officename': 'Akhara Bazar SO'}]

>>> validate(110032)   # validate(pincode)
>>> True
```
![demo](assets/demo1.gif)


<!-- LICENSE -->
## License 

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

CodewithRv - ravigoel.1997@gmail.com

Project Link: [https://github.com/ravigoel08/pyzipcin](https://github.com/ravigoel08/pyzipcin)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[contributors-url]: https://github.com/ravigoel08/pyzipcin/graphs/contributors
[forks-url]: https://github.com/ravigoel08/pyzipcin/network/members
[stars-url]: https://github.com/ravigoel08/pyzipcin/stargazers
[issues-url]: https://github.com/ravigoel08/pyzipcin/issues
[linkedin-url]: https://www.linkedin.com/in/ravi-goyal52/
[contributors-shield]: https://img.shields.io/github/contributors/ravigoel08/pyzipcin?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/ravigoel08/pyzipcin?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/ravigoel08/pyzipcin?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/ravigoel08/pyzipcin?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
