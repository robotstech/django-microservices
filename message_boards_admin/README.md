# django-microservices
![main workflow](https://github.com/iamr0b0tx/json-api/actions/workflows/main.yml/badge.svg) <br>
Microservices developed in django

## Quick Start Instructions
### Prerequisites
### Tools and Resources
1. Python 3.8+ [link](https://www.python.org/downloads/release/python-387/)
2. Virtualenv
3. Docker
4. Docker Compose

### Installation
Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions 
below

1. Create the virtual environment.
```shell script
virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.

1. Set up `.env` file by duplicating the `.example.env` file(and editing if required).

1. Activate the environment and install dependencies.
    - #### Linux
    ```shell script
    source /path/to/venv/bin/activate
    pip install -r requirements.txt
    ```

    - #### Windows
    ```cmd
    ./path/to/venv/bin/activate
    pip install -r requirements.txt
    ```
1. Launch the app
    ```shell script
    python manage.py runserver
   

## License
See list of [LICENSE](../LICENSE) 