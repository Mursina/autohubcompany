-- Create the Users table
CREATE TABLE Users (
    uid SERIAL PRIMARY KEY,
    uname VARCHAR(255) UNIQUE NOT NULL,
    upwd VARCHAR(255) NOT NULL
);

-- Create the Products table
CREATE TABLE Products (
    pid SERIAL PRIMARY KEY,
    pname VARCHAR(255) NOT NULL,
    pbrand VARCHAR(255),
    pprice DECIMAL,
    pcompat VARCHAR(255),
    pqty INT,
    pcat VARCHAR(255)
);

-- Create the CartItems table
CREATE TABLE CartItems (
    cid SERIAL PRIMARY KEY,
    uid INT REFERENCES Users(uid),
    pid INT REFERENCES Products(pid),
    cqty INT
);

-- Create the Orders table
CREATE TABLE Orders (
    oid SERIAL PRIMARY KEY,
    uid INT REFERENCES Users(uid),
    ottd DECIMAL,
    delivery_date TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create the OrderItems table
CREATE TABLE OrderItems (
    id SERIAL PRIMARY KEY,
    oid INT REFERENCES Orders(oid),
    pid INT REFERENCES Products(pid),
    oqty INT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
