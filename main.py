# building a server and usage of GET, fetching all data
from fastapi import FastAPI
from models import product

app = FastAPI()

products = [
    product(42, "Keyboard", "Mechanical keyboard", 75, 30),
    product(7, "Monitor", "27-inch 4K monitor", 299, 15),
    product(103, "Headphones", "Wireless headphones", 149, 20),
    product(21, "Tablet", "Android tablet", 250, 12),
    product(88, "Webcam", "1080p HD webcam", 59, 40),
    product(3, "Printer", "Wireless inkjet printer", 180, 8),
    product(156, "Smartwatch", "Fitness tracking watch", 120, 35),
    product(64, "Microphone", "USB condenser microphone", 89, 18),
    product(12, "SSD", "1TB NVMe SSD", 110, 22),
    product(205, "Router", "Dual-band Wi-Fi router", 65, 14),
    product(31, "Graphics Card", "Gaming GPU", 599, 7),
    product(99, "Power Bank", "20000mAh power bank", 35, 50),
    product(14, "Speakers", "Bluetooth speakers", 45, 28),
    product(73, "Laptop Stand", "Adjustable aluminum stand", 25, 60),
    product(8, "USB Hub", "7-port USB hub", 30, 45),
    product(121, "External HDD", "2TB external hard drive", 80, 16),
    product(55, "Gaming Chair", "Ergonomic gaming chair", 220, 5),
    product(240, "Mouse Pad", "Extended gaming mouse pad", 19, 70),
    product(16, "Power Supply", "750W power supply", 95, 11),
    product(67, "Cooling Fan", "RGB case cooling fan", 22, 33)
]


@app.get("/")
def greet():
    return "Welcome to my homepage"


@app.get("/products")
def get_all_product():
    return products


# 1. Get an individual product using a fixed path
@app.get("/product/1")
def get_by_id():
    return products[0]


# This is a fixed route and always returns the first list item.
# It does not search using the product's actual ID.


# 2. Dynamic path using the list index
@app.get("/product/dy/{id}")
def get_by_id_dy(id: int):
    return products[id - 1]


# This works by list position, not actual product ID.
# It can fail if the requested position is outside the list.


