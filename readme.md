# 🚚 Shipping Management System (Flask + PostgreSQL)

A web-based **Shipping Management System** built using **Flask** and **PostgreSQL** to manage customers, products, orders, payments, shipping, and delivery officers.
This application is designed to handle end-to-end order processing—from product ordering to payment and shipment tracking.

---

## 🛠 Tech Stack

* **Backend:** Python (Flask)
* **Database:** PostgreSQL
* **ORM / Migration:** SQLAlchemy
* **Authentication:** Username & Password based login
* **Database Version:** PostgreSQL 13+

---

## 📦 Core Modules

### 👤 User Management

* Admin
* Customer
* Delivery Officer
* Login & role-based access (`user_type`)

### 🛍 Product Management

* Product catalog
* Unique product codes
* Pricing support

### 📑 Order Management

* Order creation
* Product-to-customer mapping
* Unique order numbers

### 💳 Payment Management

* Multiple payment modes (Credit Card, Debit Card, Wallet)
* Payment reference tracking
* Order-payment relationship

### 🚚 Shipping Management

* Shipping assignment to delivery officers
* Shipping status tracking
* Shipping cost calculation
* Shipment date tracking

---

## 🗂 Database Schema Overview

### Main Tables

| Table Name         | Description                             |
| ------------------ | --------------------------------------- |
| `login`            | User authentication and role management |
| `admin`            | Admin profile details                   |
| `customer`         | Customer information                    |
| `delivery_officer` | Delivery personnel details              |
| `products`         | Product catalog                         |
| `orders`           | Orders placed by customers              |
| `payment`          | Payment details for orders              |
| `payment_type`     | Payment methods                         |
| `shipping`         | Shipping records                        |
| `shipping_details` | Item-level shipping details             |
| `alembic_version`  | Database migration versioning           |

---

## 🔗 Entity Relationships

* **Customer → Orders** (One-to-Many)
* **Orders → Products** (Many-to-One)
* **Orders → Payment** (One-to-One)
* **Payment → Shipping** (One-to-One)
* **Shipping → Delivery Officer** (Many-to-One)
* **Login → Admin / Customer** (One-to-One)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/shipping-management-system.git
cd shipping-management-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Update `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/shipping_db"
```

### 5️⃣ Restore Database

```bash
psql -U postgres -d shipping_db -f shipping_db_dump.sql
```

### 6️⃣ Run the Application

```bash
flask run
```

or

```bash
python run.py
```

---

## 🔐 Authentication & Roles

| User Type | Description              |
| --------- | ------------------------ |
| `1`       | Admin / Delivery Officer |
| `2`       | Customer                 |

Each user must exist in the `login` table before accessing the system.

---

## 🚀 Future Enhancements

* JWT-based authentication
* Role-based API authorization
* Shipment tracking UI
* Email/SMS notifications
* Dashboard analytics
* Integration with external payment gateways