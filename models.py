class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Vehicle:
    def __init__(self, model, available=True):
        self.model = model
        self.available = available

class Rental:
    def __init__(self, customer_id, vehicle_id, rental_date, return_date=None):
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.rental_date = rental_date
        self.return_date = return_date
