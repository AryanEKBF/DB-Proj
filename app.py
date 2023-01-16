from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import jwt

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'online_shop'
app.config['MYSQL_HOST'] = 'localhost' 
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

if __name__ == '__main__':
    app.run(debug=True)
