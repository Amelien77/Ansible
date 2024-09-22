import mysql.connector
import os
import pytest

def test_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'), 
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'your_password'), 
        database=os.getenv('DB_NAME', 'magento_db')
    )
    
    assert conn.is_connected()
    conn.close()
