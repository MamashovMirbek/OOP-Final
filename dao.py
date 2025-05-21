import sqlite3

class CustomerDAO:
    def add_customer(self, customer):
        conn = sqlite3.connect('rental_system.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", (customer.name, customer.email))
        conn.commit()
        conn.close()

class VehicleDAO:
    def add_vehicle(self, vehicle):
        conn = sqlite3.connect('rental_system.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Vehicles (model, available) VALUES (?, ?)", (vehicle.model, int(vehicle.available)))
        conn.commit()
        conn.close()

    def set_availability(self, vehicle_id, status):
        conn = sqlite3.connect('rental_system.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE Vehicles SET available = ? WHERE id = ?", (int(status), vehicle_id))
        conn.commit()
        conn.close()

class RentalDAO:
    def rent_vehicle(self, rental):
        conn = sqlite3.connect('rental_system.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Rentals (customer_id, vehicle_id, rental_date, return_date)
            VALUES (?, ?, ?, ?)
        ''', (rental.customer_id, rental.vehicle_id, rental.rental_date, rental.return_date))
        cursor.execute("UPDATE Vehicles SET available = 0 WHERE id = ?", (rental.vehicle_id,))
        conn.commit()
        conn.close()
