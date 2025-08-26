# Docker-py-api

This is a simple Python Flask application for testing purposes.

## How to run the project

### For local development

1.  **Build the Docker image:**
    ```bash
    docker build -t docker-py-api .
    ```

2.  **Run the container:**
    Use the following command to remove any old container and run the new one:
    ```bash
    docker rm -f docker-py-api
    docker run -d -p 8080:5000 --name docker-py-api docker-py-api
    ```

3.  **Access the application:**
    Once the container is running, you can access the application at [http://localhost:8080](http://localhost:8080).

## API Endpoints

-   `GET /`: Returns "Hello World!"
-   `GET /api/v1/users`: Returns a list of users.

## About Me
![Aguirre Daniels](https://github.com/daguigonz/resources/raw/main/branding/AD.png)
- Twitter: [@daguigonz](https://x.com/daguigonz)
- Newsletters: [aguirredaniels.com](https://aguirredaniels.com/)
