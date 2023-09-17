# AutoHub

## Requirements
Python 3.9+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m autohubcompany
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/swagger.json
```


## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t autohubcompany .

# starting up a container
docker run -p 8080:8080 autohubcompany
```