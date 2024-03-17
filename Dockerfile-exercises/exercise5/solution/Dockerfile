FROM node:lts-alpine as build
RUN --mount=type=bind,src=package.json,target=package.json \
    npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine3.17-slim
COPY --from=build build/ /usr/share/nginx/html/
EXPOSE 80
