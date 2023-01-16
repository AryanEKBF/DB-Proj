INSERT INTO categories (id, title, parentId)
VALUES
(1, 'Category 1', null),
(2, 'Category 2', null),
(3, 'Category 3', null),
(4, 'Category 4', null),
(5, 'Category 5', null);
INSERT INTO products (title)
VALUES
('Product 1'),
('Product 2'),
('Product 3'),
('Product 4'),
('Product 5'),
('Product 6'),
('Product 7'),
('Product 8'),
('Product 9'),
('Product 10'),
('Product 11'),
('Product 12'),
('Product 13'),
('Product 14'),
('Product 15'),
('Product 16'),
('Product 17'),
('Product 18'),
('Product 19'),
('Product 20');
INSERT INTO product_category (product_id, category_id)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 2),
(6, 2),
(7, 2),
(8, 3),
(9, 3),
(10, 3),
(11, 3),
(12, 4),
(13, 4),
(14, 4),
(15, 5),
(16, 5),
(17, 5),
(18, 5),
(19, 5),
(20, 5);

-- insert into vendors
INSERT INTO vendors (title, city, phone_number) VALUES ('vendor 1', 'New York City', '09999999991');
INSERT INTO vendors (title, city, phone_number) VALUES ('vendor 2', 'New York City', '09999999992');
INSERT INTO vendors (title, city, phone_number) VALUES ('vendor 3', 'New York City', '09999999993');
INSERT INTO vendors (title, city, phone_number) VALUES ('vendor 4', 'Los Angeles', '09999999994');
INSERT INTO vendors (title, city, phone_number) VALUES ('vendor 5', 'Los Angeles', '09999999995');

-- insert into item
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (1, 1, 20, 250.99, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (2, 1, 45, 750, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (3, 1, 98, 550, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (4, 1, 60, 650, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (5, 2, 1, 150, 50);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (6, 2, 10, 350, 20);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (7, 2, 7, 10, 49);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (8, 2, 50, 35, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (9, 3, 43, 45, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (10, 3, 84, 55.5, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (11, 3, 21, 65.80, 4);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (12, 3, 16, 15, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (13, 4, 89, 26.30, 4);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (14, 4, 10, 47, 4);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (15, 4, 13, 99, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (16, 4, 42, 610, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (17, 5, 15, 210, 0);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (18, 5, 30, 43, 10);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (19, 5, 12, 2, 11);
INSERT INTO items (product_id, vendor_id, quantity, price, discount_percentage) VALUES (20, 5, 10, 60.12, 0);

INSERT INTO users (first_name, last_name, phone_number, email, username, password, registeredAt, date_of_birth, city)
VALUES 
    ("Tim", "Jones", "(230) 449-1635", "timJ22@google.couk", "tim_jones2022", "12345678", "2022-12-02", "2000-03-11", "New York City"),
    ("Sarah", "White", "1-325-582-3684", "sarahwhite8798@icloud.couk", "real_sarah_white", "hkfhfuhf", "2021-12-02", "1997-07-11", "Los Angeles"),
    ("Pam", "Brown", "1-403-675-4872", "pam_non@google.org", "pameeela9", "poiuytrr", "2020-04-16", "1990-12-13", "Los Angeles");
INSERT INTO users (first_name, last_name, email, username, password, date_of_birth, city)
VALUES 
    ("Ed", "Sheeran", "ed.facilisis@icloud.net", "ed_the_singer", "singsong", "2010-08-22", "Texas"),
    ("Ed", "Smith", "ed.smith@yahoo.org", "ed", "Woodland", "1970-01-03", "Texas"),
    ("Regina", "Phalange", "reggie_phalange@hotmail.edu", "vegetableLover", "99999999", "1980-11-03", "New York City"),
    ("Reed", "Holmes", "reed_holmes@protonmail.org", "reedHolmesUsername", "password", "1995-11-26", "Cleveland"),
    ("Cora", "Glass", "cora.glass@outlook.ca", "cora7878", "password", "2001-06-13", "Utah"),
    ("Regina", "Peters", "regina_p2020@protonmail.com", "regina", "reginaaa", "1989-09-01", "Cleveland"),
    ("Yoshio", "Burks", "yoshio@google.com", "yoshioburks5:", "password", "1972-07-28", "New York City"),
    ("Patrick", "Mayes", "patrick@yahoo.net", "username", "12345678", "1992-02-19", "Washington DC");
INSERT INTO users (first_name, last_name, phone_number, username, password, city)
VALUES
    ("Taylor", "Swift", "1-581-766-7243", "nottherealtaylor", "passworD", "Honolulu"),
    ("Hop", "Hoffman", "(711) 884-0291", "hophoffman_10", "PlOkIjUH", "Utah"),
    ("Gideon", "Franklin", "1-323-473-4002", "FranklinTheBest", "iute8993", "Honolulu"),
    ("Elvis", "Gaines", "(312) 328-3335", "elvis_gaines01011", "password", "Texas");
INSERT INTO users (first_name, last_name, email, phone_number, admin, username, password, city)
VALUES
    ("Annabeth", "Mays", "anna.magna@protonmail.com", "1-325-582-3684", 1, "annaTheAdmin", "UTGh2kkj", "New York City"),
    ("Clive", "Harper", "clive_harper@jmail.com", "12345678", 1, "harper", "PASWORDD", "Los Angeles");

-- orders
INSERT INTO orders (user_id, paid, datePaid) VALUES(1, 1, NOW());
INSERT INTO orders (user_id, paid, datePaid) VALUES(2, 1, NOW());
INSERT INTO orders (user_id, paid, datePaid) VALUES(10, 1, NOW());
INSERT INTO orders (user_id, paid, datePaid) VALUES(5, 0, NULL);
INSERT INTO orders (user_id, paid, datePaid) VALUES(14, 1, NOW());
INSERT INTO orders (user_id, paid, datePaid) VALUES(11, 0, '2021-12-2 23:50:59');
INSERT INTO orders (user_id, paid, datePaid) VALUES(10, 0, '2020-8-8 15:10:00');
INSERT INTO orders (user_id, paid, datePaid) VALUES(12, 0, '2022-1-1 1:00:00');

-- order_item
INSERT INTO order_item (order_id, item_id)
VALUES
    (1,5),
    (1,8),
    (2,19),
    (3,12),
    (4,11),
    (5,7),
    (6,20),
    (7,17),
    (8,7),
    (8,8),
    (8,1);

INSERT INTO product_review (product_id, user_id, rating, createdAt, content)
VALUES
    (3, 11, 5, "2020-04-12", "Very good product, I use it all the time."),
    (8, 11, 5, "2020-04-14", "I bought this product, I am very happy with it."),
    (15, 11, 5, "2020-04-15", "It is expensive, but worth the money! I keep it on my bedroom wall and I always like to look at it."),
    (1, 11, 5, "2020-04-20", "You should totally buy this too, It has good quality."),
    (17, 11, 1, "2020-04-22", "HORRIBLE! It does not look like the pictures on the website AND it doesn't even work! I am never buying anything from this shop ever again."),
    (15, 11, 3, "2020-05-01", NULL),
    (15, 2, 2, "2020-01-30", NULL),
    (15, 5, 1, "2021-10-10", NULL);
INSERT INTO product_review (product_id, user_id, rating)
VALUES
    (17,13,2),
    (4,11,2),
    (18,5,3),
    (11,7,3),
    (19,7,3),
    (17,8,5),
    (12,14,3),
    (16,16,5),
    (16,12,3),
    (14,2,1),
    (4,15,3),
    (9,2,3),
    (15,14,4),
    (8,5,4),
    (20,17,4),
    (4,2,1),
    (14,10,2),
    (10,12,2),
    (16,10,2),
    (3,12,4),
    (10,17,4),
    (3,10,1),
    (14,9,3),
    (17,15,1),
    (15,11,2),
    (9,8,2),
    (11,8,5),
    (18,16,1),
    (13,10,1),
    (8,3,2),
    (18,1,3),
    (9,1,1),
    (2,10,2),
    (1,3,2),
    (10,16,2),
    (14,13,3),
    (9,11,1),
    (10,2,5),
    (8,7,2),
    (18,8,3),
    (14,13,3),
    (9,13,1),
    (10,2,5),
    (8,7,2),
    (18,8,3);
