# django-microservices
![main workflow](https://github.com/iamr0b0tx/json-api/actions/workflows/main.yml/badge.svg) <br>
Microservices developed in django

## Service
1. Message Boards
2. Message Board Images
3. Message Board Comments
4. A postgres service is also set up with three databases. See [here](https://github.com/mrts/docker-postgresql-multiple-databases)

## Quick Start Instructions
### Prerequisites
### Tools and Resources
1. Python 3.8+ [link](https://www.python.org/downloads/release/python-387/)
2. Virtualenv
3. Docker
4. Docker Compose


### Installation
1. Message Boards. See [Readme](message_boards/README.md)
2. Message Board Images. See [Readme](message_board_images/README.md)
3. Message Board Comments. See [Readme](message_board_comments/README.md)

### Run Project
```shell
docker-compose up
```

#### development
```shell
docker-compose up --build --remove-orphans
```


## License
See list of [LICENSE](LICENSE) 