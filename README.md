# TechBuy Buildroom Prototype

This repository contains a minimal prototype for a digital kanban board and
system checklist used by the TechBuy buildroom. It allows tracking of orders
and per-system checklist steps.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Initialize the database:

```bash
flask --app app.py initdb
```

3. Run the development server:

```bash
flask --app app.py run
```

The application will be available at `http://localhost:5000`.
