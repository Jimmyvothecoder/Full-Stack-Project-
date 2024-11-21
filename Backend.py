import flask
from flask import jsonify
from flask import request
import mysql.connector


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Database connection
db_config = {
    'host': 'cis2368identifier1.cposem4a2i5v.us-east-2.rds.amazonaws.com',
    'user': 'admin',
    'password': 'cis2024jim',
    'database': 'cis2368db'
}

# create a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Investor CRUD operations
# create a API for POST method for the investor table
@app.route('/investor', methods=['POST'])
def create_investor():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO investor (firstname, lastname) VALUES (%s, %s)", (data['firstname'], data['lastname']))
    conn.commit()
    return jsonify({"message": "Investor created"}), 201

# create a API for PUT method for the investor table
@app.route('/investor/<int:id>', methods=['PUT'])
def update_investor(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE investor SET firstname=%s, lastname=%s WHERE id=%s", (data['firstname'], data['lastname'], id))
    conn.commit()
    return jsonify({"message": "Investor updated"}), 200

# create a API for DELETE method for the investor table
@app.route('/investor/<int:id>', methods=['DELETE'])
def delete_investor(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM investor WHERE id=%s", (id,))
    conn.commit()
    return jsonify({"message": "Investor deleted"}), 200

# create a API for GET method for the investor table
@app.route('/investor/<int:id>', methods=['GET'])
def get_investor(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM investor WHERE id=%s", (id,))
    investor = cursor.fetchone()
    if investor:
        return jsonify({"id": investor[0], "firstname": investor[1], "lastname": investor[2]}), 200
    else:
        return jsonify({"message": "Investor not found"}), 404

# Stock CRUD operations
# create a API for POST method for the stock table
@app.route('/stock', methods=['POST'])
def create_stock():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stock (stockname, abbreviation, currentprice) VALUES (%s, %s, %s)", (data['stockname'], data['abbreviation'], data['currentprice']))
    conn.commit()
    return jsonify({"message": "Stock created"}), 201

# create a API for PUT method for the stock table
@app.route('/stock/<int:id>', methods=['PUT'])
def update_stock(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE stock SET stockname=%s, abbreviation=%s, currentprice=%s WHERE id=%s", (data['stockname'], data['abbreviation'], data['currentprice'], id))
    conn.commit()
    return jsonify({"message": "Stock updated"}), 200

# create a API for DELETE method for the stock table
@app.route('/stock/<int:id>', methods=['DELETE'])
def delete_stock(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stock WHERE id=%s", (id,))
    conn.commit()
    return jsonify({"message": "Stock deleted"}), 200

# Bond CRUD operations
# create a API for POST method for the bond table
@app.route('/bond', methods=['POST'])
def create_bond():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bond (bondname, abbreviation, currentprice) VALUES (%s, %s, %s)", (data['bondname'], data['abbreviation'], data['currentprice']))
    conn.commit()
    return jsonify({"message": "Bond created"}), 201

# create a API for PUT method for the bond table
@app.route('/bond/<int:id>', methods=['PUT'])
def update_bond(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE bond SET bondname=%s, abbreviation=%s, currentprice=%s WHERE id=%s", (data['bondname'], data['abbreviation'], data['currentprice'], id))
    conn.commit()
    return jsonify({"message": "Bond updated"}), 200

# create a API for DELETE method for the bond table
@app.route('/bond/<int:id>', methods=['DELETE'])
def delete_bond(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bond WHERE id=%s", (id,))
    conn.commit()
    return jsonify({"message": "Bond deleted"}), 200

# View investor portfolio
# create a API for GET method to view the investor table portfolio
@app.route('/investor/<int:id>/portfolio', methods=['GET'])
def get_portfolio(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # get stocks portfolio
    cursor.execute("SELECT stock.stockname, isp.current_quantity FROM investor_stock_portfolio isp JOIN stock ON isp.stockid = stock.id WHERE isp.investorid=%s", (id,))
    stocks = cursor.fetchall()
    
    # get bonds portfolio
    cursor.execute("SELECT bond.bondname, ibp.current_quantity FROM investor_bond_portfolio ibp JOIN bond ON ibp.bondid = bond.id WHERE ibp.investorid=%s", (id,))
    bonds = cursor.fetchall()
    
    return jsonify({
        "stocks": [{"stockname": stock[0], "current_quantity": stock[1]} for stock in stocks],
        "bonds": [{"bondname": bond[0], "current_quantity": bond[1]} for bond in bonds]
    }), 200

# Transaction (buy/sell stock)
## create a API for POST method to buy/sell stocks
@app.route('/investor/<int:id>/transaction/stock', methods=['POST'])
def stock_transaction(id):
    data = request.json  # Expecting { "stock_id": int, "quantity": int }
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if investor exists (Ensure the query returns only one row)
    cursor.execute("SELECT id FROM investor WHERE id=%s LIMIT 1", (id,))
    investor = cursor.fetchone()
    if not investor:
        return jsonify({"error": "Invalid investor ID"}), 400

    # Check if stock exists (Ensure the query returns only one row)
    cursor.execute("SELECT id FROM stock WHERE id=%s LIMIT 1", (data['stock_id'],))
    stock = cursor.fetchone()
    if not stock:
        return jsonify({"error": "Invalid stock ID"}), 400

    # Handle the transaction (buy or sell)
    try:
        # Call the stored procedure to handle the stock transaction
        cursor.callproc('handle_stock_transaction', [id, data['stock_id'], data['quantity']])
        conn.commit()

        # Success message
        if data['quantity'] > 0:
            return jsonify({"message": "Stock purchase successful"}), 200
        else:
            return jsonify({"message": "Stock sale successful"}), 200

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400

    finally:
        cursor.close()
        conn.close()






# Transaction (buy/sell bond)
# create a API for POST method to buy/sell bonds
@app.route('/investor/<int:id>/transaction/bond', methods=['POST'])
def bond_transaction(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if investor exists
    cursor.execute("SELECT * FROM investor WHERE id=%s", (id,))
    investor = cursor.fetchone()
    if not investor:
        return jsonify({"error": "Invalid investor ID"}), 400
    
    # Check if bond exists
    cursor.execute("SELECT * FROM bond WHERE id=%s", (data['bond_id'],))
    bond = cursor.fetchone()
    if not bond:
        return jsonify({"error": "Invalid bond ID"}), 400

    # Insert bond transaction if IDs are valid
    cursor.execute("INSERT INTO bondtransaction (investorid, bondid, quantity) VALUES (%s, %s, %s)", (id, data['bond_id'], data['quantity']))
    conn.commit()
    return jsonify({"message": "Bond transaction successful"}), 200


# Cancel transaction (stock)
@app.route('/transaction/stock/<int:transaction_id>', methods=['DELETE'])
def delete_stock_transaction(transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stocktransaction WHERE id=%s", (transaction_id,))
    conn.commit()
    return jsonify({"message": "Stock transaction deleted"}), 200

# Cancel transaction (bond)
@app.route('/transaction/bond/<int:transaction_id>', methods=['DELETE'])
def delete_bond_transaction(transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bondtransaction WHERE id=%s", (transaction_id,))
    conn.commit()
    return jsonify({"message": "Bond transaction deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)