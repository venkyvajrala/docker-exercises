# Exercise 3 Solution

```yaml
services:
  web:
    build: .
    ports:
      - 5001:5000
    networks:
      - movies_default

networks:
  movies_default:
      external: true
```

### Service Configuration (web):
- <b>build: .:</b> Specifies the build context for the web service, indicating the current directory.
- <b>ports:</b> Maps port 5001 of the host to port 5000 of the container for accessing the application.
- <b>networks:</b> Specifies the network to which the service should connect.
    - <b>movies_default:</b> Indicates the name of the network.
#### Network Configuration (movies_default):
- <b>external: true:</b> Specifies that the network is external to the current Docker Compose file.

### Explanation:
- #### Connecting to External Network:
    - <b>By specifying networks:</b> movies_default with external: true, Docker Compose searches for the specified network outside of the current Compose file.
    - This configuration enables App2 to connect to the Redis database created by App1, as they share the same external network.
- <b>Network Name Matching: </b> 
    - The networks section ensures that App2 is connected to the network named movies_default, which must be created externally (presumably by App1). </br></br>

This solution demonstrates how to configure Docker Compose to connect containers in different Compose files by leveraging external networks, enabling communication between applications while adhering to the exercise requirements.
