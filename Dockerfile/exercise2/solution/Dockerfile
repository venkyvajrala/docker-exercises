FROM alpine:3.19.1

ARG secret_code

RUN apk update && apk add --no-cache \
    curl

RUN export STATUS_CODE=${secret_code} && \
    curl -s -o response.jpg https://http.dog/${STATUS_CODE}.jpg && \
    unset STATUS_CODE

CMD [ "sh", "-c","echo secret is ${STATUS_CODE}" ]
