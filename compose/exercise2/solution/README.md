# Compose exercise2 solution

## Docker Compose Configuration
```yaml
services:
  web:
    build: 
      context: .
    ports: 
      - 8080:5000
    environment:
      FLASK_DEBUG: true
      VERSION: "${USERNAME:?error}/${USER_EMAIL:?error}/${TAG:-latest}"
```

## Solution Details

### Service Configuration (web):
<b> - build: context: .:</b> Specifies the build context for the web service, indicating the current directory.<br>
<b> - ports:</b>  Maps port 8080 of the host to port 5000 of the container for accessing the Flask application.<br>
<b> - environment:</b>  Sets environment variables for the service. <br>
  - <b> FLASK_DEBUG: true:</b>  Enables Flask debugging.<br>
  - <b> Interpolated Variable (VERSION):</b> 
    - <b>${USERNAME:?error}:</b> Interpolates the USERNAME environment variable. If `USERNAME` is not set, it throws an error message "error".
    - <b> ${USER_EMAIL:?error}:</b>  Interpolates the USER_EMAIL environment variable. If `USER_EMAIL` is not set, it throws an error message "error".
    - <b> ${TAG:-latest}:</b>  Interpolates the TAG environment variable. If TAG is not set, it defaults to "latest".

More details here: https://docs.docker.com/compose/environment-variables/env-file/