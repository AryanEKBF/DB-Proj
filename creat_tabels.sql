#CREATE DATABASE online_shop;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(50),
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(8) NOT NULL,
    admin TINYINT DEFAULT 0,
    registeredAt DATETIME DEFAULT NOW(),
    date_of_birth DATE,
    city VARCHAR(15)
);

CREATE TABLE categories (
    id INT PRIMARY KEY NOT NULL,
    title VARCHAR(50) NOT NULL,
    parentId INT,
    FOREIGN KEY (parentId) REFERENCES categories(id)
);

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL
);

CREATE TABLE product_category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    category_id INT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE vendors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    city VARCHAR(15) NOT NULL,
    phone_number VARCHAR(15)
);

CREATE TABLE items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    vendor_id INT,
    quantity INT NOT NULL,
    price FLOAT(5, 2) NOT NULL,
    discount_percentage INT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (vendor_id) REFERENCES vendors(id),
    CONSTRAINT valid_numbers CHECK (price >= 0 AND discount_percentage <= 100 AND discount_percentage >= 0 AND quantity >= 0)
);

CREATE TABLE product_review (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    parent_id INT,
    user_id INT,
    rating INT,
    createdAt DATETIME DEFAULT NOW(),
    content TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (parent_id) REFERENCES product_review(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    CHECK (rating <= 5 AND rating >= 0)
);

CREATE TABLE carts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE cart_item (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cart_id INT,
    item_id INT,
    FOREIGN KEY (cart_id) REFERENCES carts(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    dateOrdered DATETIME NOT NULL DEFAULT NOW(),
    paid TINYINT DEFAULT 0,
    datePaid DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_item (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    item_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);