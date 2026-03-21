class SQLQuery:
    def __init__(self, query: str, parameters: dict = None):
        self.query = query
        self.parameters = parameters if parameters else {}

    def execute(self, connection):
        with connection.cursor() as cursor:
            cursor.execute(self.query, self.parameters)
            return cursor.fetchall()  

    def __str__(self):
        return f"SQLQuery(query={self.query}, parameters={self.parameters})"