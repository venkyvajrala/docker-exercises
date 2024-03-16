# Exercise4: Solution

1. #### Using Python as Base Image  
Let's utilize the Python base image:
```Dockerfile
FROM python:alpine3.18
```
Since the version needs to be from a build argument, let's rewrite it to use a dynamic version:

```Dockerfile
ARG python_version
FROM python:${python_version}
```

2. #### Creating Required Non-Root User and Group <br>
It's a best practice to run application as non root user.
To ensure proper permissions, let's create the required non-root user and group:
```Dockerfile
RUN addgroup -g 1000 calc && \
    adduser -h /home/calc -s /bin/sh -u 1000 -G calc -D calc && \
    mkdir -p /home/calc/src/app && \
    chown -R calc:calc /home/calc/
```

Now, let's make the user and group dynamic:
```Dockerfile
# Set user and group arguments
ARG user=calc
ARG group=${user}
ARG user_id=1000
ARG group_id=${user_id}
ARG app_dir=src/app

# Create user,group and directories with user permissions set
RUN addgroup -g ${group_id} ${group} && \
    adduser -h /home/${user} -s /bin/sh -u ${user_id} -G ${group} -D ${user} && \
    mkdir -p /home/${user}/src/app && \
    chown -R ${user}:${group} /home/${user}/
```

3. #### Selecting the Non-Root User Created

Let's switch to the non-root user:
```Dockerfile
# Switch to non root user
USER ${user}
```

4. #### Setting Working Directory

Set the working directory:
```Dockerfile
# Set working directory 
WORKDIR /home/${user}/src/app
```

5. #### Copying Source Code <br>
When copying files in Docker, permissions relative to the   target directory remain unchanged, and instead, Docker retains the permissions from the source. To ensure that the copied files have the correct permissions according to our user, we use the `--chown` flag. This approach is beneficial as it reduces the need for an additional layer to change permissions using RUN and chown.
```Dockerfile
# Copy main.py
COPY --chown=${user}:${group} main.py .
```

6. #### Installing Dependencies <br>
We could have utilized the COPY instruction, but it's unnecessary because we don't want the `requirements.txt` file to exist in the final image. It's only needed while installing packages for this particular `RUN` instruction. This approach also reduces the number of layers in the image.
```Dockerfile
RUN  --mount=type=bind,src=requirements.txt,target=requirements.txt \
    pip3 install -r requirements.txt
```

7. #### Setting Application Entry Point and Default Arguments <br>
In this configuration, we are setting `--help` as the default command in `CMD`. This allows us to override this argument at runtime if needed, while also providing a default output to display the help section when the container is run.
```Dockerfile
ENTRYPOINT [ "python","main.py"]
CMD [ "--help" ]
```


The final Dockerfile should resemble the following:

```Dockerfile
ARG python_version
FROM python:${python_version}

# Set user and group arguments
ARG user=calc
ARG group=${user}
ARG user_id=1000
ARG group_id=${user_id}
ARG app_dir=src/app

# Create user,group and directories with user permissions set
RUN addgroup -g ${group_id} ${group} && \
    adduser -h /home/${user} -s /bin/sh -u ${user_id} -G ${group} -D ${user} && \
    mkdir -p /home/${user}/src/app && \
    chown -R ${user}:${group} /home/${user}/

# Switch to non root user
USER ${user}

# Set working directory 
WORKDIR /home/${user}/src/app

# Copy main.py
COPY --chown=${user}:${group} main.py .

# Install dependencies
RUN  --mount=type=bind,src=requirements.txt,target=requirements.txt \
    pip3 install -r requirements.txt

# Set application entryponint and default argument
ENTRYPOINT [ "python","main.py"]
CMD [ "--help" ]
```