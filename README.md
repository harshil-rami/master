# master
Machine Learning Project

To set-up CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = 
2. HEROKU_API_KEY = 
3. HEROKU_APP_NAME = 

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname>
```

>Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```commandline
docker run -p 5000:5000 -e PORT=5000 ce93f34a8e8e
```
To check run container in docker
```commandline
docker ps
```
To stop docker container
```commandline
docker stop <container_id>
```