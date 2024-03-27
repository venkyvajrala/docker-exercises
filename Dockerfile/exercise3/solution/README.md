# Excercise 3 solution:

Here's the rewritten content with the necessary modifications:

```Dockerfile
FROM alpine:3.19.1

RUN apk update && apk add --no-cache \
    curl \
    jq

ARG website_url="https://jsonplaceholder.typicode.com/posts"

RUN ["/bin/sh", "-c", "set -o pipefail && curl ${website_url} | grep \"title\" | sort | uniq > titles.txt" ]

CMD [ "sh","-c","cat titles.txt" ]
```

## Explanation:

- In the modified Dockerfile, we prepend set -o pipefail && to the curl command to ensure that the build process fails if any command in the pipe fails unexpectedly.
- Additionally, we include the shell /bin/sh and the -c option explicitly to ensure compatibility across different shells.
- With these modifications, the Dockerfile ensures that the build process fails if any command in the pipe fails unexpectedly, thus adhering to the best practice of using set -o pipefail to prevent inadvertent build success.
