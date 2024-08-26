import psycopg2 # type: ignore

def fetch_clients():
    connection = psycopg2.connect(
        host='192.168.1.18',
        user='',
        password='',
        dbname=''
    )
    cursor = connection.cursor()
    cursor.execute("SELECT name, email FROM clients")
    clients = cursor.fetchall()
    connection.close()
    return clients
