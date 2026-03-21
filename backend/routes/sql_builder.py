# SQL Builder

# This module provides functions for building SQL queries in a dynamic and flexible way.

class SQLBuilder:
    def __init__(self):
        self.query = ""

    def select(self, columns):
        if isinstance(columns, list):
            columns = ", ".join(columns)
        self.query = f"SELECT {columns}"
        return self

    def from_table(self, table):
        self.query += f" FROM {table}"
        return self

    def where(self, condition):
        self.query += f" WHERE {condition}"
        return self

    def order_by(self, column, asc=True):
        direction = "ASC" if asc else "DESC"
        self.query += f" ORDER BY {column} {direction}"
        return self

    def build(self):
        return self.query

# Example usage:
# builder = SQLBuilder()
# query = builder.select(['name', 'age']).from_table('users').where('age > 18').order_by('name').build()  
# print(query)  # Outputs: SELECT name, age FROM users WHERE age > 18 ORDER BY name ASC