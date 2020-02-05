# BigMood
A mini app that returns the data visualization of emotions from an image url using the Microsoft Azure Face API.

![gif](https://j.gifs.com/nxVrKY.gif)

## Getting Started
### Installation
* Clone repository

    `$ git clone https://github.com/dominiquecuevas/BigMood`

* Create a Virtual Environment

    `$ virtualenv env`

    Command if on a Windows machine:

    `$ virtualenv env --always-copy`

* Obtain a Face API key on a 7-day trial https://azure.microsoft.com/en-us/services/cognitive-services/face/

* Create a secrets.sh file with your key

    `$ touch secrets.sh`

    Copy code into the file:

    ```export FACE_KEY=[YOUR KEY]```

* Activate virtual environment

    `$ source env/bin/activate`

* Load key into shell environment

    `$ source secrets.sh`

* Install dependances

    `$ pip install -r requirements.txt`

* Run the app

    `$ python3 server.py`