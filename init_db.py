import sqlite3

def init_db():
    conn = sqlite3.connect('rental_system.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT NOT NULL,
            available INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rentals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            vehicle_id INTEGER,
            rental_date TEXT,
            return_date TEXT,
            FOREIGN KEY(customer_id) REFERENCES Customers(id),
            FOREIGN KEY(vehicle_id) REFERENCES Vehicles(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
