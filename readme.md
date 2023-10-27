![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# Test Task repository

---

## How to start
First of all, start the API as the Memory Alarm script creates a POST request to it.
### 1. Run API

in *root* directory:
```sh
make init
```
then in *api* directory :
```
docker-compose build
docker-compose up
```

### 2. Run memory alarm script

in *root* directory:

```sh
make build-alarm
make run-alarm
```

## Usage
The Flask application runs on *http://localhost:8080*.  
It provides **GET**, **POST**, **PUT** requests to *http://localhost:8080/api/v1/memories*.

---

Memory Alarm script sent **POST** request with actual RAM usage, when it more than 500mb.
