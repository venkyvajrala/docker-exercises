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
