```yaml
services:
  web:
    build: .
    ports: 
      - 8080:5000
    env_file:
      - app.env
    environment:
      FLASK_DEBUG: true
    develop:
      watch:
        - path: app.py
          target: /src/app/app.py
          action: sync
        - path: requirements.txt
          action: rebuild

  redis:
    image: redis:alpine3.19
```

## Solution Details:
### Development Service Configuration (web):

- <b>build: .</b> : Specifies the build context for the web service, indicating the current directory.
- <b>ports:</b> Maps port 8080 of the host to port 5000 of the container for accessing the Flask application.
- <b>env_file:</b> Specifies an external file (app.env) containing environment variables to be used by the service.
- <b>environment:</b> Sets the FLASK_DEBUG environment variable to true, enabling Flask debugging.
### - Develop Configuration:
- <b>watch:</b> Configures file watching for development purposes.
- <b>path:</b> app.py: Specifies the path to watch for changes in the app.py file.
- <b>target:</b> /src/app/app.py: Defines the target path inside the container where the app.py file will be synchronized.
- <b>action:</b> sync: Specifies that changes to app.py should trigger synchronization with the container without restarting it.
- <b>path:</b> requirements.txt: Indicates the path to monitor changes in the requirements.txt file.
- <b>action: rebuild:</b> Specifies that modifications to requirements.txt should trigger a rebuild of the container.

More details are here : https://docs.docker.com/compose/file-watch/