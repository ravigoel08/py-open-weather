from setuptools import setup,find_packages
with open("README.md", "r") as fh:
  long_description = fh.read()
setup(
  name = 'py-open-weather',         # How you named your package folder (MyLib)
  packages=find_packages(),
  include_package_data=True,
  version = '0.1.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python3 library providing information of Current & Forecast of Weather as well as Air Pollution based on data from OpenWeatherMap.',
  long_description = long_description,   # Give a long description about your library
  long_description_content_type = "text/markdown",
  author = 'CodewithRv',                   # Type in your name
  author_email = 'ravigoel.1997@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ravigoel08/py-open-weather',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['open weather api', 'owm', 'weather','weather api', 'pyweather', 'open weather', 'air pollution', 'py-open-weather'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'pydantic',
          'orjson',
      ],
  classifiers=[
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
    "Operating System :: OS Independent",
  ],
)