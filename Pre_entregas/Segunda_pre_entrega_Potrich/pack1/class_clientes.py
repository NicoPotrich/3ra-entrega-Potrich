

class Client:
    """
    Represents a standard client with basic information.
    """
    def __init__(self, name, last_name, age, email):
        # Initialize client attributes
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email

    def __str__(self):
        # Return a string representation of the client
        return f"Client: {self.name} {self.last_name}."
    
    def make_purchase(self, producto):
        # Method to simulate a purchase made by the client
        return f"The client {self.name} {self.last_name} has purchased '{producto}'\nAn email has been sent to {self.email} with the details of the purchase."

    def return_product(self, product):
        # Method to simulate returning a non-refundable product
        return f"The client {self.name} {self.last_name} isn't VIP, the product {product} is non-refundable."


class Client_vip(Client):
    """
    Represents a VIP client with additional discount features.
    """
    def __init__(self, name, last_name, age, email, level):
        # Initialize VIP client attributes, inheriting from Client
        super().__init__(name, last_name, age, email)
        self.level = level
    
    def __str__(self):
        # Return a string representation of the VIP client
        return f"Client VIP: {self.name} {self.last_name} ({self.level})."

    def get_discount(self, mount):
        # Method to calculate and return discount based on VIP level
        if self.level == "gold":
            discount = f"The amount with the discount is ${mount * 0.9}"
        elif self.level == "platinum":
            discount = f"The amount with the discount is ${mount * 0.85}"
        else:
            discount = f"The amount with the discount is ${mount}"
        return  discount

    def return_product(self, product):
        # Override method to simulate returning a product by a VIP client
        return f"The client {self.name} {self.last_name} has returned: '{product}'."

