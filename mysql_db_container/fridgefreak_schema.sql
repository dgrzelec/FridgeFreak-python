create database fridgefreak;
use fridgefreak;

CREATE TABLE IF NOT EXISTS products (
id int NOT NULL AUTO_INCREMENT,
name text,
quantity int DEFAULT NULL,
category text,
storage_space text,
expire_by date DEFAULT NULL,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS test_products LIKE products;

TRUNCATE test_products;

