# FastAPI GET Requests — Learning Notes

> Learning how to create GET endpoints and retrieve product data using FastAPI.

## 1. Creating the server

In `main.py`:

```python
from fastapi import FastAPI
from models import product

app = FastAPI()
```

- `FastAPI` is used to create the application.
- `product` is imported from `models.py`.
- `app = FastAPI()` creates the application instance.

## 2. Product data

The `products` list contains multiple product objects.

Each product has:

- ID
- Name
- Description
- Price
- Quantity

**Important:** Product IDs are not in sequential order. For example, the first product has ID `42`, but its list index is `0`.

## 3. GET — Homepage

In `main.py`, find `greet()`.

```python
@app.get("/")
def greet():
    return "Welcome to my homepage"
```

- `@app.get("/")` creates a GET endpoint for the homepage.
- The function returns a welcome message.

URL: `/`

## 4. GET — Fetch all products

In `main.py`, find `get_all_product()`.

```python
@app.get("/products")
def get_all_product():
    return products
```

This endpoint returns the entire product list.

URL: `/products`

## 5. Fixed path — Fetch one list item

In `main.py`, find `get_by_id()`.

```python
@app.get("/product/1")
def get_by_id():
    return products[0]
```

- The URL is fixed.
- `products[0]` returns the first item in the list.
- It does not search for the product whose actual ID is `1`.

This approach is useful for understanding a basic endpoint, but it is not a flexible ID-based lookup.

## 6. Dynamic path — Using a list index

In `main.py`, find `get_by_id_dy()`.

```python
@app.get("/product/dy/{id}")
def get_by_id_dy(id: int):
    return products[id - 1]
```

- `{id}` is a path parameter.
- `id: int` tells FastAPI to treat the parameter as an integer.
- `id - 1` converts a one-based position into a zero-based Python list index.

Example:

- `/product/dy/1` returns the first item.
- `/product/dy/2` returns the second item.

**Limitation:** This uses the list position, not the actual product ID. An invalid position can cause an error.

## 7. Dynamic path — Searching by actual product ID

In `main.py`, find `get_product_by_id()`.

```python
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return f"Product {id}: Not Found"
```

How it works:

1. The loop visits each product in the list.
2. `product.id == id` compares the actual product ID with the requested ID.
3. If a match is found, that product is returned.
4. If no match is found, the not-found message is returned.

Examples:

- `/product/42` returns the Keyboard.
- `/product/7` returns the Monitor.
- `/product/999` returns a not-found message.

In a production API, use an HTTP 404 response for a missing product.

## 8. Why are the paths different?

The fixed route is `/product/1`.

The index-based route is `/product/dy/{id}`.

The actual-ID route is `/product/{id}`.

The `dy` segment keeps the index experiment separate from the actual-ID route.

## 9. Running the application

From the folder containing `main.py`, run:

```powershell
python -m uvicorn main:app --reload
```

Open these URLs:

- Homepage: `http://127.0.0.1:8000/`
- All products: `http://127.0.0.1:8000/products`
- API testing: `http://127.0.0.1:8000/docs`

## Key takeaway

**List index and product ID are different things.**

- Index identifies an item's position in a list.
- ID identifies the product itself.
- Searching by the actual ID works even when IDs are non-sequential.

10. PUT — Update a Product

@app.put("/products")
def update_product(id: int, Product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = Product
            return "Product updated successfully"

    return "Product not found"

- "@app.put()" — Updates an existing product.
- "id: int" — Receives the product ID through a query parameter.
- "Product: product" — Receives new product details in the request body.
- "products[i].id == id" — Checks whether the product ID matches.
- "products[i] = Product" — Replaces the entire product.
- "return" — Stops function execution.
- If no match is found, returns ""Product not found"".

11. DELETE — Delete a Product

@app.delete("/products")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"

    return "Product not found"

- "@app.delete()" — Deletes an existing product.
- "id: int" — Receives the product ID.
- "products[i].id == id" — Checks whether the product exists.
- "del products[i]" — Removes the product from the list.
- If no match is found, returns ""Product not found"".

3. Important Concepts

- "products" — List containing product objects.
- "products[i]" — Accesses a product using its index.
- "products[i].id" — Accesses the product's ID.
- "range(len(products))" — Generates the list indexes.
- "return" — Immediately exits the function.
- In-memory list: Data is lost when the server restarts.

Quick Revision

Method| Purpose
GET| Retrieve data
POST| Add data
PUT| Update/replace data
DELETE| Remove data