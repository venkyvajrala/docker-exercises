FROM alpine:3.19.1

RUN apk update && apk add --no-cache \
    curl \
    jq

ARG website_url="https://jsonplaceholder.typicode.com/posts"

RUN ["/bin/sh", "-c", "set -o pipefail && curl ${website_url} | grep \"title\" | sort | uniq > titles.txt" ]

CMD [ "sh","-c","cat titles.txt" ]
