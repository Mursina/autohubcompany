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

## Create a database in the PostgreSQL DB

Please follow the below steps to create a database
1. Login through the default postgres user
   ```
    sudo -iu postgres psql
   ```
2. Create a database(In our case, it is autohubcompany)
   ```
   CREATE DATABASE autohubcompany;
   ```
3. Create an user with password
   ```
   CREATE USER mur WITH PASSWORD '1234';
   ```
4. Give the privileges to the created user
   ```
   GRANT ALL PRIVILEGES ON DATABASE autohubcompany TO mur;
   ```
5. Create the tables using sql file
   ```
   psql --username=postgres autohubcompany < /mnt/d/mur_dev/autohub/my_db.sql
   ```
6. Connect to the database
   ```
   \c autohubcompany
   ```

## Get the packages for running the application
Create a virtualenv:
```
virtualenv penv -p /usr/bin/python3.9
```

Activate it:
```
. penv/bin/activate
```

Install required packages:
```
pip install -r requirements.txt
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t autohubcompany .

# starting up a container
docker run -p 8080:8080 autohubcompany
```