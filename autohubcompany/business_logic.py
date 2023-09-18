from flask import jsonify
import psycopg2

class BusinessLogic:

    def __init__(self):
        # Initialize the database connection in the constructor
        self.conn = psycopg2.connect(
            host="localhost",
            database="autohubcompany",
            user='mur',
            password=1234
        )

    def add_products_to_store(self, body):
        try:
            cur = self.conn.cursor()

            for product in body:
                cur.execute('INSERT INTO Products (pname, pbrand, pprice, pcompat, pqty, pcat)'
                            'VALUES (%s, %s, %s, %s, %s, %s)',
                            (product.name,
                             product.brand,
                             product.price,
                             product.compatibility,
                             product.quantity,
                             product.category)
                            )

            self.conn.commit()
            return "Successfully Added", 201
        
        except Exception as e:
            return jsonify(error=str(e)), 500

    def get_products_from_store(self):
        try:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM Products')

            results = cur.fetchall()
            products_list = []
            for row in results:
                part_id, name, brand, price, compatibility, quantity, category = row
                product_dict = {
                    "part_id": part_id,
                    "name": name,
                    "price": float(price),
                    "brand": brand,
                    "compatibility": compatibility,
                    "quantity": quantity,
                    "category": category
                }
                products_list.append(product_dict)

            return products_list

        except Exception as e:
            return jsonify(error=str(e)), 500
        
    def get_product_from_store(self, product_id):
        cur = self.conn.cursor()
        cur.execute(f'SELECT * FROM Products where pid={product_id}')
        results = cur.fetchall()

        products_list = []
        for row in results:
            part_id, name, brand, price, compatibility, quantity, category = row
            product_dict = {
                "part_id": part_id,
                "name": name,
                "price": float(price),
                "brand": brand,
                "compatibility": compatibility,
                "quantity": quantity,
                "category": category
            }
            products_list.append(product_dict)

        return products_list
    
    def get_products_from_cart(self, user_id):
        
        try:
            cur = self.conn.cursor()
            cur.execute(f'''
                        SELECT u.uname AS user_name, p.pname, p.pbrand, p.pprice, p.pcompat, ci.cqty, p.pcat
                        FROM CartItems ci
                        INNER JOIN Products p ON ci.pid = p.pid
                        INNER JOIN Users u ON ci.uid = u.uid
                        WHERE ci.uid = {user_id};
                        ''')

            results = cur.fetchall()
            formatted_results = {
                'user_name': None,
                'products': []
            }

            for row in results:
                user_name, pname, pbrand, pprice, pcompat, pqty, pcat = row
                if formatted_results['user_name'] is None:
                    formatted_results['user_name'] = user_name

                formatted_results['products'].append({
                    'name': pname,
                    'brand': pbrand,
                    'price': float(pprice),  # Convert to float for JSON serialization
                    'compatibility': pcompat,
                    'quantity': pqty,
                    'category': pcat
                })

            return formatted_results

        except Exception as e:
            return jsonify(error=str(e)), 500
        
    def add_product_to_cart(self, body):
        try:

            user_id = body.user_id
            product_id = body.product_id
            quantity = body.quantity

            cur = self.conn.cursor()
            cur.execute(f'''
                        SELECT pname,pqty FROM Products WHERE pid = {product_id}
                        ''')
            results = cur.fetchall()

            if results[0][1] is None:
                self.conn.commit()
                return f"Product {results[0][0]} is not found", 404
            elif results[0][1] < quantity:
                self.conn.commit()
                return f"We only have {results[0][1]} items of {results[0][0]}", 404
            else:
                cur.execute('INSERT INTO CartItems (uid, pid, cqty)'
                                    'VALUES (%s, %s, %s)',
                                    (user_id,
                                    product_id,
                                    quantity)
                                    )

            self.conn.commit()
            return "Successfully added to the cart", 201

        except Exception as e:
            return jsonify(error=str(e)), 500
    
    def remove_user_cart(self, user_id):
        try:
            cur = self.conn.cursor()
            cur.execute(f'DELETE FROM CartItems WHERE cid={user_id}')
            self.conn.commit()
            return jsonify(message='Cart items deleted successfully'), 204

        except Exception as e:
            return jsonify(error=str(e)), 500
        
    def update_product_quantity_to_cart(self, body):
        try:
            cur = self.conn.cursor()

            for cart_item in body:
                cart_id = cart_item['cart_id']
                quantity = cart_item['quantity']
                cur.execute(f'''
                            SELECT pname,pqty FROM Products
                            ''')
                results = cur.fetchall()

                if results[0][1] is None:
                    self.conn.commit()
                    return f"Product {results[0][0]} is not found", 404
                elif results[0][1] < quantity:
                    self.conn.commit()
                    return f"We only have {results[0][1]} items of {results[0][0]}", 404
                else:
                    cur.execute(f'UPDATE CartItems SET cqty = {quantity} WHERE cid = {cart_id};')

            self.conn.commit()
            return "Quantities are updated", 200

        except Exception as e:
            return jsonify(error=str(e)), 500
        
    def place_an_order(self, body):
        try:
            cur = self.conn.cursor()

            delivery_date = body['delivery_date']
            user_id = body['user_id']
            updated_cart = body['updated_cart']

            updated_status = self.update_product_quantity_to_cart(updated_cart)

            if updated_status[1] == 200:
                total_amount = 0
                # find the total amount
                for item in updated_cart:
                    cart_id = item["cart_id"]
                    quantity = item["quantity"]

                    cur.execute(f'''
                        SELECT p.pprice
                        FROM CartItems ci
                        INNER JOIN Products p ON ci.pid = p.pid
                        WHERE ci.cid = {cart_id};
                    ''')
                    result = cur.fetchone()

                    if result is not None:
                        product_price = result[0]
                        total_amount += product_price * quantity

                cur.execute(f'INSERT INTO Orders (uid, ottd, delivery_date) VALUES ({user_id}, {total_amount}, {delivery_date}) RETURNING oid')
                order_id = cur.fetchone()[0]

                for item in updated_cart:
                    cart_id = item["cart_id"]
                    quantity = item["quantity"]

                    cur.execute(f'SELECT pid FROM CartItems WHERE cid = {cart_id}')
                    product_id = cur.fetchone()[0]

                    cur.execute('INSERT INTO OrderItems (oid, pid, oqty) VALUES (%s, %s, %s)',
                                (order_id, product_id, quantity))

                self.conn.commit()
                return "Order successfully updated", 201
            
            else:
                return updated_status
        except Exception as e:
            return jsonify(error=str(e)), 500
        
    def add_users(self, body):
        cur = self.conn.cursor()

        import secrets

        password = secrets.token_hex(6)
        for user in body:
            cur.execute('INSERT INTO Users (uname, upwd)'
                        'VALUES (%s, %s)',
                        (user,
                         password)
                        )

        self.conn.commit()
        return "Successfully Added", 201

    def __del__(self):
        # Destructor to ensure the connection is closed when the object is deleted
        if hasattr(self, 'conn') and self.conn is not None:
            self.conn.close()
