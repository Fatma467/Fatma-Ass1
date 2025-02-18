class Customer:
    """Represents a customer who places delivery orders."""

    def __init__(self, customer_id, name, contact, address, email):
        # Initialize customer details with private attributes
        self.__customer_id = customer_id  # Unique identifier for the customer
        self.__name = name  # Customer's name
        self.__contact = contact  # Customer's contact number
        self.__address = address  # Customer's address
        self.__email = email  # Customer's email

    # Getters to access private attributes
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    # Setters to update private attributes
    def set_contact(self, contact):
        self.__contact = contact  # Update customer's contact number

    def set_address(self, address):
        self.__address = address  # Update customer's address

    def set_email(self, email):
        self.__email = email  # Update customer's email

    def place_order(self, order):
        """Places a new delivery order."""
        print(f"Order placed: {order}")

    def view_orders(self):
        """Displays all placed orders."""
        print("Viewing orders...")


class DeliveryOrder:
    """Represents a delivery order placed by a customer."""

    def __init__(self, order_id, recipient, package_details, status, customer_id):
        # Initialize order details with private attributes
        self.__order_id = order_id  # Unique identifier for the order
        self.__recipient = recipient  # Recipient details
        self.__package_details = package_details  # Package information
        self.__status = status  # Current order status
        self.__customer_id = customer_id  # Associated customer ID

    # Getters to access private attributes
    def get_order_id(self):
        return self.__order_id

    def get_recipient(self):
        return self.__recipient

    def get_package_details(self):
        return self.__package_details

    def get_status(self):
        return self.__status

    def get_customer_id(self):
        return self.__customer_id

    # Setters to update private attributes
    def set_status(self, status):
        self.__status = status  # Update order status

    def set_package_details(self, package_details):
        self.__package_details = package_details  # Update package details

    def confirm_order(self):
        """Confirms the delivery order."""
        print("Order confirmed.")

    def cancel_order(self):
        """Cancels the delivery order."""
        print("Order canceled.")


class DeliveryStaff:
    """Represents the delivery staff responsible for order deliveries."""

    def __init__(self, staff_id, name, assigned_orders, contact, location):
        # Initialize delivery staff details with private attributes
        self.__staff_id = staff_id  # Unique identifier for delivery staff
        self.__name = name  # Staff name
        self.__assigned_orders = assigned_orders  # List of assigned orders
        self.__contact = contact  # Staff contact number
        self.__location = location  # Current location of the staff

    # Getters to access private attributes
    def get_staff_id(self):
        return self.__staff_id

    def get_name(self):
        return self.__name

    def get_assigned_orders(self):
        return self.__assigned_orders

    def get_contact(self):
        return self.__contact

    def get_location(self):
        return self.__location

    # Setters to update private attributes
    def set_contact(self, contact):
        self.__contact = contact  # Update staff contact number

    def set_location(self, location):
        self.__location = location  # Update staff location

    def update_delivery_status(self, order_id, status):
        """Updates the delivery status of an order."""
        print(f"Updated order {order_id} status to {status}.")

    def view_assigned_orders(self):
        """Displays assigned deliveries."""
        print("Viewing assigned deliveries...")


class Admin:
    """Represents an admin who manages orders and assigns delivery staff."""

    def __init__(self, admin_id, name, contact, email, role):
        # Initialize admin details with private attributes
        self.__admin_id = admin_id  # Unique identifier for admin
        self.__name = name  # Admin name
        self.__contact = contact  # Admin contact number
        self.__email = email  # Admin email
        self.__role = role  # Role of the admin (Manager, Supervisor, etc.)

    # Getters to access private attributes
    def get_admin_id(self):
        return self.__admin_id

    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    def get_email(self):
        return self.__email

    def get_role(self):
        return self.__role

    # Setters to update private attributes
    def set_contact(self, contact):
        self.__contact = contact  # Update admin contact number

    def set_email(self, email):
        self.__email = email  # Update admin email

    def set_role(self, role):
        self.__role = role  # Update admin role

    def manage_orders(self):
        print("Managing orders...")

    def assign_delivery_staff(self, staff_id, order_id):
        print(f"Assigned delivery staff {staff_id} to order {order_id}.")
