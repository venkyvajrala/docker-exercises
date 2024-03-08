# Exercise-1 Solution

Create `Dockerfile` with below content
```Dockerfile
FROM alpine:3.19.1
LABEL application="ping" \
      com.example.version=0.5 \
      env="dev"

RUN apk update && apk add --no-cache \
    curl \
    git \
    iputils-ping

CMD ["sh","-c","curl www.example.com"]
```

Run below command to build the image where Dockerfile is placed.
```shell
docker build -t curl:0.5 .
```
Now you should be able to use the image to create containers and also perform image filtering

```shell
docker images --filter "label=env=dev" --filter "label=application=ping" --filter "label=com.example.version=0.5"
```

```shell
docker run -it curl:0.5
```

### Best practices used:

- Always place multiline package installation or labels in alphabetical order for better readability and prevent duplicate package installations
- While installing packages remove cache to reduce image size and place them all in single line RUN command. Read [here](https://docs.docker.com/develop/develop-images/instructions/#label) for more info.


