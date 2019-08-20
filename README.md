# Static JSON response
A Flask app to return a bit of JSON on HTTP GET/POST/PUT. Requires docker.

## Run app

    make build
    make run

Test it using curl:

    curl -X POST http://localhost:8080

## Push to Docker Registry

Build and push to repository:

    make build
    make push
