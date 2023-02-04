from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
import jwt

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'online_shop'
app.config['MYSQL_HOST'] = 'localhost' 
app.secret_key = 'super secret key'
mysql = MySQL(app)

@app.route('/product_categories', methods=['GET'])
def product_categories():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM product_category;''')
        rv = cur.fetchall()
        return jsonify(rv)

@app.route('/best_sellings_month', methods=['GET'])
def best_sellings_month():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT prod.title, COUNT(prod.title) AS total
                        FROM (SELECT products.title
                            FROM products, items, order_item, orders
                            WHERE products.id = items.product_id AND items.id = order_item.item_id AND orders.id = order_item.order_id AND orders.dateOrdered >= DATE_SUB(NOW(), INTERVAL 1 MONTH))
                            AS prod
                        GROUP BY prod.title
                        ORDER BY total DESC''')
        rv = cur.fetchall()
        return jsonify(rv)

@app.route('/best_sellings_week', methods=['GET'])
def best_sellings_week():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT prod.title, COUNT(prod.title) AS total
                       FROM (SELECT products.title
                           FROM products, items, order_item, orders
                           WHERE products.id = items.product_id AND items.id = order_item.item_id AND orders.id = order_item.order_id AND orders.dateOrdered >= DATE_SUB(NOW(), INTERVAL 1 MONTH))
                           AS prod
                       GROUP BY prod.title
                       ORDER BY total DESC''')
        rv = cur.fetchall()
        return jsonify(rv)

@app.route('/comments_in_products', methods=['GET'])
def comments_in_products():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT products.title, product_review.content, users.username
                       FROM products, product_review, users
                       WHERE products.id = product_review.product_id AND product_review.user_id = users.id''')
        rv = cur.fetchall()
        return jsonify(rv)

@app.route('/cheapest_sellers_for_admin', methods=['GET'])
def cheapest_sellers_for_admin():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT tmp.ptitle, tmp.vtitle, MIN(tmp.price) AS price
                       FROM
                           (SELECT products.title AS ptitle, vendors.title AS vtitle, items.price AS price, users.admin AS admin, users.id AS uid
                           FROM items, products, vendors, users
                           WHERE items.product_id = products.id AND items.vendor_id = vendors.id AND users.admin = 1) AS tmp
                       GROUP BY tmp.ptitle, tmp.vtitle
                       ORDER BY tmp.ptitle, tmp.vtitle;''')
        rv = cur.fetchall()
        return jsonify(rv)

@app.route('/register', methods=['POST'])
def register():
    cur = mysql.connection.cursor()
    data = request.get_json()
    cur.execute("INSERT INTO users (first_name, last_name, phone_number, email, username, password) VALUES (%s, %s, %s, %s, %s, %s)", (data['first_name'], data['last_name'], data['phone_number'], data['email'], data['username'], data['password']))
    try:
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'New user created!'})
    except:
        return jsonify({'message': 'Error'})

# The admin should have the ability to update normal users
#
#@app.route('/user_from_admin', methods=['PUT', 'GET', 'DELETE'])
#def user_from_admin():
#    cur = mysql.connection.cursor()
#    if request.method == 'GET':
#        is_admin = False
#        is_admin2 = False
#
#        data = request.get_json()
#        cur.execute("SELECT admin FROM users WHERE username = %s AND password = %s", (data['username'], data['password']))
#        try:
#            rv = cur.fetchall()
#            if rv[0][0] == 1:
#                    is_admin = True
#        except:
#            return "Wrong username or password"
#
#        username2 = data['username2']
#        #cur = mysql.connection.cursor()
#        cur.execute("SELECT admin FROM users WHERE username = %s", (username2,))
#        try:
#            rv2 = cur.fetchall()
#            if rv2[0][0] == 1:
#                is_admin2 = True
#        except:
#            return "Wrong username or password"
#        
#        print(is_admin)
#        print(is_admin2)
#        if is_admin == True and is_admin2 == False:
#            is_ok = True
#            return "OK, you can update this user"
#        else:
#            return "You can't update this user"
#
#    elif request.method == 'PUT':
#        print(is_ok)
#        if is_ok == True:
#            is_ok = False
#            data = request.get_json()
#            cur.execute("UPDATE users SET first_name = %s, last_name = %s, phone_number = %s, email = %s, date_of_birth = %s, city = %s, admin = %s , WHERE username = %s", (data['first_name'], data['last_name'], data['phone_number'], data['email'], data['date_of_birth'], data['city'], data['admin'], username2)) 
#            try:
#                mysql.connection.commit()
#                cur.close()
#                return jsonify({'message': 'User information updated!'})
#            except:
#                return jsonify({'message': 'Error'})
#        else:
#            print("Error")
#            return jsonify({'message': 'Error'})
#    else:
#        if is_ok == True:
#            is_ok = False
#            cur.execute("DELETE FROM users WHERE username = %s", (username2))
#            try:
#                mysql.connection.commit()
#                cur.close()
#                return jsonify({'message': 'User deleted!'})
#            except:
#                return jsonify({'message': 'Error'})
#        else:
#            return jsonify({'message': 'Error'})
#
#
#
# 
@app.route('/user_from_admin', methods=['PUT', 'DELETE'])
def user_from_admin():
    if request.method == 'PUT':
        is_ok = False
        cur = mysql.connection.cursor()
        data = request.get_json()
        # is the user admin?
        cur.execute("SELECT admin FROM users WHERE username = %s AND password = %s", (data['username'], data['password']))
        rv = cur.fetchall()
        # is user2 admin?
        cur.execute("SELECT admin FROM users WHERE username = %s", (data['username2'],))
        rv2 = cur.fetchall()
        print(rv)
        print(rv2)
        try:
            if rv[0][0] == 1 and rv2[0][0] == 0:
                is_ok = True
        except:
            return jsonify({'message': 'Error'})
        if is_ok:
            # update user2 first_name, last_name, phone_number, email, date_of_birth, city, address, password, admin
            cur.execute("UPDATE users SET first_name = %s, last_name = %s, phone_number = %s, email = %s, date_of_birth = %s, city = %s, password = %s, admin = %s WHERE username = %s", (data['first_name'], data['last_name'], data['phone_number'], data['email'], data['date_of_birth'], data['city'], data['password2'], data['admin'], data['username2']))
            try:
                mysql.connection.commit()
                cur.close()
                return jsonify({'message': 'User updated!'})
            except:
                return jsonify({'message': 'Error'})
        else:
            return jsonify({'message': 'Error'})         
    else:
        is_ok = False
        cur = mysql.connection.cursor()
        data = request.get_json()
        # is the user admin?
        cur.execute("SELECT admin FROM users WHERE username = %s AND password = %s", (data['username'], data['password']))
        rv = cur.fetchall()
        # is user2 admin?
        cur.execute("SELECT admin FROM users WHERE username = %s", (data['username2'],))
        rv2 = cur.fetchall()
        print(rv)
        print(rv2)
        try:
            if rv[0][0] == 1 and rv2[0][0] == 0:
                is_ok = True
        except:
            return jsonify({'message': 'Error'})
        if is_ok:
            cur.execute("DELETE FROM users WHERE username = %s", (data['username2'],))
            try:
                mysql.connection.commit()
                cur.close()
                return jsonify({'message': 'User deleted!'})
            except:
                return jsonify({'message': 'Error'})
        else:
            return jsonify({'message': 'Error'})


#query1
@app.route('/products', methods=['GET'])
def products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT title FROM products")
    rv = cur.fetchall()
    return jsonify(rv)

#query4
@app.route('/orders', methods=['GET'])
def orders():
    cur = mysql.connection.cursor()
    cur.execute("SELECT orders.dateOrdered, products.title," +
    " users.first_name, users.last_name FROM orders, order_item, items, products, users" +
    " WHERE orders.user_id = users.id AND orders.id = order_item.order_id AND" +
    " order_item.item_id = items.id AND items.product_id = products.id")
    rv = cur.fetchall()
    return jsonify(rv)

#query7
@app.route('/special_offers', methods=['GET'])
def special_offers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT products.title, items.price, items.discount_percentage, items.id" +
    " FROM products, items WHERE items.product_id = products.id AND" +
    " items.discount_percentage > 15")
    rv = cur.fetchall()
    return jsonify(rv)

#query10
@app.route('/categories', methods=['GET'])
def categories():
    cur = mysql.connection.cursor()
    cur.execute("SELECT products.title, categories.title" +
    " FROM product_category, products, categories" + 
    " WHERE product_category. product_id = products.id AND" + 
    " product_category.category_id = categories.id")
    rv = cur.fetchall()
    return jsonify(rv)

#query13
@app.route('/top3', methods=['GET'])
def top3():
    cur = mysql.connection.cursor()
    cur.execute("SELECT content, rating FROM product_review" + 
    " WHERE content IS NOT NULL ORDER BY rating DESC LIMIT 3")
    rv = cur.fetchall()
    return jsonify(rv)

#log in
@app.route('/log_in', methods=['POST'])
def log_in():
    msg = ''
    username = request.json['username']
    password = request.json['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users"+
    " WHERE username = %s AND password = %s", (username, password))
    account = cur.fetchone()
    if account:
        session['loggedin'] = True
        session['id'] = account[0]
        session['username'] = account[5]
        msg = 'Logged in successfully !'
    else:
        msg = 'Incorrect username / password !'
    return jsonify({'msg': msg})
    
#edit product
@app.route('/edit_product', methods=['POST'])
def edit_product():
    cur = mysql.connection.cursor()
    cur.execute('SELECT admin FROM users '+
    'WHERE id = %s', (session['id'],))
    admin = cur.fetchone()
    if admin[0] :
        product_id = request.json['product_id']
        item_id = request.json['item_id']
        quantity = request.json['quantity']
        price = request.json['price']
        discount_percentage = request.json['discount_percentage']
        title = request.json['title']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE items SET quantity = %s, price = %s,"+
        " discount_percentage = %s WHERE id = %s AND product_id = %s",
         (quantity, price, discount_percentage, item_id, product_id))
        cur.execute("UPDATE products SET title = %s WHERE id = %s",(title, product_id))
        try :
            mysql.connection.commit()
            return jsonify({'status': 'success'})
        except :
            return jsonify({'status': 'unsuccessful'})
    else :
        return jsonify({'msg': 'You are not an admin'})


#QUERY14 : 3 reviews with lowest rating for product
@app.route('/three_lowest_rating_reviews', methods=['GET', 'POST'])
def product_categories():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        data = request.get_json()
        cur.execute(f"SELECT p.id, p.title, pr.user_id, u.username, pr.rating, pr.content, pr.createdAt FROM product_review AS pr INNER JOIN products AS p ON pr.product_id = p.id INNER JOIN users AS u ON pr.user_id = u.id WHERE pr.product_id = {data['pr.product_id']} ORDER BY rating LIMIT 3;")
        rv = cur.fetchall()
        return jsonify(rv)

#QUERY15 : sold amount of item by month
@app.route('/item_sold_monthly', methods=['GET'])
def item_sold_monthly():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT YEAR(o.datePaid) AS year_column, MONTH(o.datePaid) AS month_column, SUM(i.price - i.price * i.discount_percentage / 100) AS total_sold
        FROM orders AS o
        INNER JOIN order_item AS oi ON o.id = oi.order_id
        INNER JOIN items AS i ON i.id = oi.item_id
        WHERE o.paid = 1
        AND i.id = 1
        AND o.datePaid IS NOT NULL
        GROUP BY YEAR(o.datePaid), MONTH(o.datePaid)
        ORDER BY YEAR(o.datePaid), MONTH(o.datePaid) DESC;''')
        rv = cur.fetchall()
        return jsonify(rv)

#query16 : average price of total items sold by month
@app.route('/average_items_sold_monthly', methods=['GET'])
def average_items_sold_monthly():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT YEAR(o.datePaid) AS year_column, MONTH(o.datePaid) AS month_column, AVG(i.price - i.price * i.discount_percentage / 100) AS average_sold FROM orders AS o INNER JOIN order_item AS oi ON o.id = oi.order_id INNER JOIN items AS i ON i.id = oi.item_id WHERE o.paid = 1 AND o.datePaid IS NOT NULL GROUP BY YEAR(o.datePaid), MONTH(o.datePaid) ORDER BY YEAR(o.datePaid), MONTH(o.datePaid) DESC;")
        rv = cur.fetchall()
        return jsonify(rv)

#query17 : users from same city
@app.route('/users_same_city', methods=['GET', 'POST'])
def users_same_city():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        data = request.get_json()
        cur.execute(f"SELECT id, first_name, last_name, email, username, city FROM users WHERE city = {data['city']};")
        rv = cur.fetchall()
        return jsonify(rv)

#query18 : vendors from same city
@app.route('/vendors_same_city', methods=['GET'])
def vendors_same_city():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        data = request.get_json()
        cur.execute(f"SELECT id, title, city FROM vendors WHERE city = {data['city']};")
        rv = cur.fetchall()
        return jsonify(rv)

# add product for admin
@app.route('/add_product', methods=['POST'])
def add_product():
    cur.execute(f"SELECT admin FROM users WHERE id = {session['id']};")
    admin = cur.fetchone()
    if admin :
        cur = mysql.connection.cursor()
        data = request.get_json()
        cur.execute(f"INSERT INTO products (title) VALUES ({data['title']});")
        try :
            mysql.connection.commit()
            return jsonify({'status': 'success'})
        except :
            return jsonify({'status': 'unsuccessful'})
    else :
        return jsonify({'msg': 'You are not an admin'})

#edit user info
@app.route('/edit_my_info', methods=['POST'])
def edit_my_info():
    cur = mysql.connection.cursor()
    data = request.get_json()
    cur.execute(f"UPDATE users SET first_name = {data['first_name']}, last_name = {data['last_name']}, phone_number = {data['phone_number']}, email = {data['email']}, username = {data['username']}, password = {data['password']}, date_of_birth = {data['date_of_birth']}, city = {data['city']} WHERE id = {data['id']};")
    try :
        mysql.connection.commit()
        return jsonify({'status': 'success'})
    except :
        return jsonify({'status': 'unsuccessful'})



if __name__ == '__main__':
    app.run(debug=True)
