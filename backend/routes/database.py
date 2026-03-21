from flask import Blueprint, request, jsonify
import sqlite3
 
# Create a new Blueprint for database routes
database_bp = Blueprint('database', __name__)
 
# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')  # Modify the path as needed
    conn.row_factory = sqlite3.Row
    return conn
 
# Route to execute SQL commands
@database_bp.route('/execute_sql', methods=['POST'])
def execute_sql():
    sql_query = request.json.get('query')
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(sql_query)
        conn.commit()
        result = cur.fetchall()  # Fetch results if applicable
        return jsonify({'status': 'success', 'data': [dict(row) for row in result]}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    finally:
        conn.close()
 
# Route to get data from a table
@database_bp.route('/get_data/<table_name>', methods=['GET'])
def get_data(table_name):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {table_name}')
        rows = cur.fetchall()
        return jsonify({'status': 'success', 'data': [dict(row) for row in rows]}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    finally:
        conn.close()