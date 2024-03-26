## Exercise5: Solution

```Dockerfile
FROM node:lts-alpine as build
RUN --mount=type=bind,src=package.json,target=package.json \
    npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine3.17-slim
COPY --from=build build/ /usr/share/nginx/html/
EXPOSE 80
```
### Key Considerations:

- #### Choosing the Right Base Images:
We opt for `node:lts-alpine` and `nginx:stable-alpine3.17-slim` as they are lightweight and have fewer vulnerabilities.

- #### Copying Necessary Files:
Only essential files needed to run the application are copied from the previous stages. This helps reduce the final image size and ensures that only relevant artifacts are included.
