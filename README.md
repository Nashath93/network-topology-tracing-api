# Network Topology Tracing API

A headless REST API using Django REST Framework (DRF). The API will track network infrastructure components and the physical or logical connections between them.

## Technology Stack

- Python
- Django
- Django REST Framework
- Git

# Setup, Installation and Run

## Prerequisites

The following should be installed locally:

- Python 3.12+
- pip
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/Nashath93/network-topology-tracing-api.git
cd network-topology-tracing-api
```

## Step2: Create a Python virtual environment
```bash
python -m venv .venv
```

Activate the virtual environment.

### On a MacOS / Linux machine

```bash
source .venv/bin/activate
```

### On a Windows machine

```powershell
.venv/Script/Activate.ps1
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Apply database migrations

```bash
python manage.py migrate
```

## Step 5: Run the development server

```bash
python manage.py runserver
```

This will launch Python's WSGI (Web Server Gateway Interface) development server at `http://127.0.0.1:8000/`

The API will be available at: 

```text
http://127.0.0.1:8000/api/
```
---
# Assumptions

### 1. A connection cannot loop back to the same interface
### 2. A Site object cannot be deleted while it is referenced by one or more Devices
### 3. An Interface object cannot be deleted while it is referenced as the start or end of an existing connection
### 4. SQLite database is used for local development
### 5. Postman Client is used for local API connection testing
### 6. Internet speed is represents in Mbps

---
# High-Level Design

The task models network infrastructure components using the following relational schema relationships:

Data Model Relationship Diagram is at: `./images/schema_relationship.jpeg`

```text
Site
 │
 │ 1:M
 ▼
Device
 │
 │ 1:M
 ▼
Interface
 │
 │ start / end
 ▼
Connection
```

### One to One (1:1) Relationships

* A **Device** belongs to a **Site**
* An **Interface** belongs to a **Device**

### One to Many (1:M) Relationships

* A **Site** can have multiple **Devices**
* A **Device** can have multiple **Interfaces**.

> **Note:** A **Connection** represents a strictly point-to-point conection between two **Interfasces**







