class Manufacturer:
    def __init__(self, id, name, contact, address):
        self.id = id
        self.name = name
        self.contact = contact
        self.address = address
    def details(self):
        print("Manufacturer Details:")
        print(f"ID:{self.id}\n NAME:{self.name}\n CELL:{self.contact}\n ADDRESS:{self.address}\n" )

class Supplier:
    def __init__(self, id: int, name: str, contact: str, address: str):
        self.id = id
        self.name = name
        self.contact = contact
        self.address = address
    def details(self):
        print("Supplier Details: ")
        print(f"ID:{self.id}\n NAME:{self.name}\n CELL:{self.contact}\n ADDRESS:{self.address}\n" )

class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Customer:
    def __init__(self, id: int, name: str, contact: str, email: str):
        self.id = id
        self.name = name
        self.contact = contact
        self.email = email

class Account:
    def __init__(self, id: int, type: str, username: str, password: str):
        self.id = id
        self.type = type
        self.username = username
        self.password = password

class Product:
    def __init__(self, id: int, name: str, formula: str, purchase_price: float, 
                 sale_price: float, piece_per_item: int, price_per_item: float,
                 manufacturer_id: int, supplier_id: int, category_id: int,
                 available_quantity: int, expiry: str):
        self.id = id
        self.name = name
        self.formula = formula
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.piece_per_item = piece_per_item
        self.price_per_item = price_per_item
        self.manufacturer_id = manufacturer_id
        self.supplier_id = supplier_id
        self.category_id = category_id
        self.available_quantity = available_quantity
        self.expiry = expiry

class Invoice:
    def __init__(self, invoice_id: int, total_price: float, total_discount: float,
                 grand_total: float, customer_id: int, consultant_name: str, 
                 date: str, account_id: int):
        self.invoice_id = invoice_id
        self.total_price = total_price
        self.total_discount = total_discount
        self.grand_total = grand_total
        self.customer_id = customer_id
        self.consultant_name = consultant_name
        self.date = date
        self.account_id = account_id

class InvoiceItems:
    def __init__(self, invoice_id: int, product_id: int, price_per_item: float,
                 quantity: int, total_discount: float, grand_total: float):
        self.invoice_id = invoice_id
        self.product_id = product_id
        self.price_per_item = price_per_item
        self.quantity = quantity
        self.total_discount = total_discount
        self.grand_total = grand_total

class PurchaseVoucher:
    def __init__(self, product_id: int, product_name: str, purchased_price: float,
                 qst: float, expiry: str, quantity: int):
        self.product_id = product_id
        self.product_name = product_name
        self.purchased_price = purchased_price
        self.qst = qst
        self.expiry = expiry
        self.quantity = quantity

print("Enter the details of the manufacturer:")
id = int(input("ID: "))
name = input("Name: ")
contact = input("Contact: ")
address = input("Address: ")
c1 = Manufacturer(id, name, contact, address)
c1.details()
print(c1)

print("Enter the details of the supplier:")
id = int(input("ID: "))
name = input("Name: ")
contact = input("Contact: ")
address = input("Address: ")
c2 = Supplier(id, name, contact, address)
c2.details()
print(c2)

