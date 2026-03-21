import sqlite3  # or any other SQL library you wish to use

class SQLExecutor:
    def __init__(self, db_file: str):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, params: tuple = None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()  # Commit changes if any
            return self.cursor.fetchall()  # Return results of the query if applicable
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

    def close(self):
        self.connection.close()  # Close the database connection
