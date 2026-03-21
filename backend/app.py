from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/sql-builder', methods=['GET', 'POST'])
def sql_builder():
    # Logic for SQL builder
    return jsonify({'message': 'SQL builder endpoint'}), 200

@app.route('/api/database-operations', methods=['GET', 'POST'])
def database_operations():
    # Logic for database operations
    return jsonify({'message': 'Database operations endpoint'}), 200

if __name__ == '__main__':
    app.run(debug=True)