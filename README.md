# flask-files
This python script written in flask serves a simple webpage that lists files in project's directory. 

also, It's [dockerized](https://hub.docker.com/repository/docker/rzepson/flask-files/general)

In order to build this docker image you could use buildx:

`docker buildx build -t ${DOCKER_USER}/flask-files:latest --platform linux/arm64,linux/amd64,linux/amd64/v2,linux/ppc64le,linux/s390x,linux/386,linux/arm/v7,linux/arm/v6 --push .`

Default docker port is: 5000

