# Database Schema Documentation

## Table: Users
- **id** (INT): Primary key, unique identifier for each user.
- **username** (VARCHAR): Unique username for accessing the system.
- **password** (VARCHAR): Hashed password for user authentication.
- **email** (VARCHAR): Unique email address for each user.
- **created_at** (DATETIME): Timestamp when the user was created.

## Table: Products
- **id** (INT): Primary key, unique identifier for each product.
- **name** (VARCHAR): Name of the product.
- **description** (TEXT): Description of the product.
- **price** (DECIMAL): Price of the product.
- **created_at** (DATETIME): Timestamp when the product was created.

## Table: Orders
- **id** (INT): Primary key, unique identifier for each order.
- **user_id** (INT): Foreign key, references Users(id).
- **product_id** (INT): Foreign key, references Products(id).
- **quantity** (INT): Number of products in the order.
- **created_at** (DATETIME): Timestamp when the order was created.

## Relationships
- A user can place multiple orders. (One-to-Many)
- Each order can include one product. (Many-to-One)

## Notes
- Ensure to index fields that are frequently queried for better performance.
- All sensitive information such as passwords must be encrypted before storage.