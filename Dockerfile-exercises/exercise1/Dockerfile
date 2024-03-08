FROM alpine:3.19.1
LABEL application="ping" \
      com.example.version=0.5 \
      env="dev"

RUN apk update && apk add --no-cache \
    curl \
    git \
    iputils-ping

CMD ["sh","-c","curl www.example.com"]
