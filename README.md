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
   psql --username=postgres autohubcompany < /mnt/d/mur_dev/autohubcompany/my_db.sql
   ```
6. Connect to the database
   ```
   \c autohubcompany
   ```

## Functionality
1. API functionality
   
![Alt text](image.png#center)

i. POST /users:

    This post call will get a list of user as a request body and will create password for each. Then it will be stored in Users Table

ii. POST /products:

    This will add products with info using request body and will be stored in the Products Table

iii. GET /products:

    This will give the product details which are stored in the Products Table

iv. GET /products/{product_id}:

    It will give product info for a particular id

v. POST /cart:

    Here each entry of the bucket will be stored as a record. For example, consider the request body 

        {
            "user_id": 3,
            "product_id": 2,
            "quantity": 1000
        }
    

    Here each users record per product will be stored. Database table will be,
    
    cid | uid | pid | cqty 
    -----+-----+-----+------
    1 |   3 |   2 |   10
    2 |   1 |   1 |   10
    3 |   2 |   1 |   10
    4 |   2 |   1 |   13
    5 |   3 |   1 |   13
    6 |   4 |   1 |   13

    If the quantity is greater than the stock, It will give an error message like "We only have {stock} items of {product}.
    
vi. GET /cart:

    Since the tables have relationships, each record will be shown with a readabe manner. Here we can see the cart items for a person with product info
    {
        "products": [
            {
                "brand": "FilterMaster",
                "category": "Engine Components",
                "compatibility": "Fits Toyota Camry (2012-2017)",
                "name": "Oil Filter",
                "price": 6.99,
                "quantity": 10
            },
            {
                "brand": "ACME Brakes",
                "category": "Brakes",
                "compatibility": "Fits Honda Civic (2015-2020)",
                "name": "Brake Pads",
                "price": 29.99,
                "quantity": 13
            }
        ],
        "user_name": "Charlie"
    }

vii. DELETE /cart

    It will remove an entry from the CartItems Table

viii. PATCH /cart

    The products quantity will be update as per UI's data using a request body. If the quantity is greater than stock, it will not update and will give a detailed error message like

    "We only have 100 items of Brake Pads"

ix. POST /order

    Here also, we will check the stock and we will calculate the total amount for each orders. Then it will be stored into Order Table. OrderItems Table will also updated to get all the products info there.

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

Note:

1. All screenshots are attached
2. Postman collections is stored as a json file under the swagger folder