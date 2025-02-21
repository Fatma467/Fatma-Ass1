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
        pass  # Implementation for placing an order

    def view_orders(self):
        """Displays all placed orders."""
        pass  # Implementation for viewing orders


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
        pass  # Implementation for confirming order

    def cancel_order(self):
        """Cancels the delivery order."""
        pass  # Implementation for canceling order


class DeliveryStaff:
    """Represents the delivery staff responsible for order deliveries."""

    def __init__(self, staff_id, name, contact, location, assigned_orders=[]):
        # Initialize delivery staff details with private attributes
        self.__staff_id = staff_id  # Unique identifier for delivery staff
        self.__name = name  # Staff name
        self.__contact = contact  # Staff contact number
        self.__location = location  # Current location of the staff
        self.__assigned_orders = assigned_orders  # List of assigned orders

    # Getters to access private attributes
    def get_staff_id(self):
        return self.__staff_id

    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    def get_location(self):
        return self.__location

    def get_assigned_orders(self):
        return self.__assigned_orders

    # Setters to update private attributes
    def set_contact(self, contact):
        self.__contact = contact  # Update staff contact number

    def set_location(self, location):
        self.__location = location  # Update staff location

    def update_status(self, order_id, status):
        """Updates the delivery status of an order."""
        pass  # Implementation for updating delivery status

    def view_orders(self):
        """Displays assigned deliveries."""
        pass  # Implementation for viewing assigned orders


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
        """Manages delivery orders."""
        pass  # Implementation for managing orders

    def assign_staff(self, staff_id, order_id):
        """Assigns delivery staff to an order."""
        pass  # Implementation for assigning delivery staff
# Create objects of all identified classes

# Creating a customer object
customer = Customer(customer_id=101, name="Fatma Albahri", contact="0501299919", address="29c Street, Dubai", email="fatma.albahri@gmail.com")

# Creating an order object associated with the customer
order = DeliveryOrder(order_id=5001, recipient="Shamma Ahmad", package_details="Electronics - Laptop", status="Processing", customer_id=customer.get_customer_id())

# Creating a delivery staff object
staff = DeliveryStaff(staff_id=301, name="Amna Abdulla", contact="9876543210", location="Al Khawaneej", assigned_orders=[order.get_order_id()])

# Creating an admin object
admin = Admin(admin_id=201, name="Reem Khalid", contact="5678901234", email="reem112@gmail.com", role="Manager")

# Simulating the generation of a delivery note
def generate_delivery_note(order):
    """Generates and displays the delivery note for an order."""
    print("\n--- Delivery Note ---")
    print(f"Order ID: {order.get_order_id()}")
    print(f"Recipient: {order.get_recipient()}")
    print(f"Package Details: {order.get_package_details()}")
    print(f"Order Status: {order.get_status()}")
    print(f"Customer ID: {order.get_customer_id()}")
    print(f"Delivery Staff Assigned: {staff.get_name()} ({staff.get_staff_id()})")
    print(f"Admin In-Charge: {admin.get_name()} ({admin.get_admin_id()})")
    print("---------------------\n")

# Generate and display the delivery note
generate_delivery_note(order)