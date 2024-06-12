CREATE USER 'testuser' IDENTIFIED WITH mysql_native_password BY 'testpassword';
GRANT ALL privileges on fridgefreak.test_products TO 'testuser';
CREATE USER 'fridgefreak_api' IDENTIFIED WITH mysql_native_password BY 'mypassword';
GRANT ALL privileges on fridgefreak.products TO 'fridgefreak_api';