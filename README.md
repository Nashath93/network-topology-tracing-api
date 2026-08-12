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
---
# High-Level Design

```text
Site
 │
 │ 1:N
 ▼
Device
 │
 │ 1:N
 ▼
Interface
 │
 │ start / end
 ▼
Connection
```


