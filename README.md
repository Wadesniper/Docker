# Student-List
This repo is a simple application to list student with a webserver (PHP) and API (Flask)
![image](https://user-images.githubusercontent.com/57738842/232176651-8dbe4ca0-d8c1-4fe8-b552-7fdd54eb1bbf.png)

# EN-Student-List
Introduction
This document explains the steps to dockerize the POZOS application which consists of a simple Flask API serving student ages and a PHP website that consumes the API.

## Build
The Dockerfile contains the instructions to build the API image. It installs the required dependencies, sets a volume for data storage, exposes port 5000, and starts the Flask app by running student_age.py. The student-age.json file contains the data served by the API.

To build the image, run `docker build -t api-pozos:1 ..`

After building the image, a bridge network named pozos is created by running docker network create pozos.

To start the API, run `docker run -d --network pozos --name Test-api-pozos -v ${PWD}/student_age.json:/data/student_age.json -p 4000:5000 api-pozos:1`.

To test the API, run `curl -u toto:python -X GET http://"host IP:API exposed port"/pozos/api/v1.0/get_student_ages`.

## IAC
The docker-compose.yml file deploys two services - a web UI and the API.

The web UI is served by an Apache server running on the php:apache image. It depends on the API and consumes it via authentication. The website source code is stored in the ./website directory. The environment variables USERNAME and PASSWORD are set to allow the website to authenticate with the API.

The API service is the image built in the previous step. The student_age.json file is mounted in the /data directory.

To deploy the containers, run `docker-compose up`. To remove the previously created container, run `docker rm Test-api-pozos`.

![P2](https://user-images.githubusercontent.com/57738842/232350381-c7b9624a-69a1-4d38-94da-3600474ff0d3.JPG)

## Registry
A Docker registry is used to store and distribute Docker images. Follow the instructions in the official documentation to create a Docker registry.

## Delivery
The Docker UI can be used to manage the registry. The UI can be started by running `docker run -d -p 5000:8080 --name registry-ui -e REGISTRY_URL=http://<registry IP>:<registry port>/v2 joxit/docker-registry-ui`

![P4](https://user-images.githubusercontent.com/57738842/232350822-d5b1395b-54c3-4fcc-8b5e-9dda3e61a71f.JPG)
