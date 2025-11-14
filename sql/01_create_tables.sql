DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS order_items CASCADE;

CREATE TABLE customers (
  customer_id INT,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  join_date DATE,
  region TEXT,
  segment TEXT
);

CREATE TABLE products (
  product_id INT,
  product_name TEXT,
  category TEXT,
  unit_cost NUMERIC(10,2),
  list_price NUMERIC(10,2)
);

CREATE TABLE orders (
  order_id INT,
  customer_id INT,
  order_date DATE,
  order_status TEXT
);

CREATE TABLE order_items (
  order_item_id INT,
  order_id INT,
  product_id INT,
  qty INT,
  unit_price NUMERIC(10,2),
  revenue NUMERIC(12,2)
);
