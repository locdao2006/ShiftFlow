# ShiftFlow

ShiftFlow is a self-directed web application designed to help small food-service teams organize and document daily operations.

The project was inspired by challenges I observed in a fast-paced food-service environment, where shift leaders need to track inventory, complete shift responsibilities, monitor employee training, and communicate important information between shifts.

## Features

### End-of-Day Inventory

Employees can enter the remaining quantity of each inventory item at the end of a shift.

Quick-select buttons make inventory entry faster:

- 0
- 5
- 10
- 15
- 20

Exact quantities can also be adjusted manually.

ShiftFlow automatically identifies items as:

- ✅ In Stock
- ⚠️ Low Stock
- 🚨 Out of Stock

### Shift Tasks

ShiftFlow includes a checklist for common shift responsibilities such as inventory checks, cleaning, organizing supplies, trash removal, and closing procedures.

### Training Tracker

Employee training can be tracked across four stations:

- Prep
- Barista
- Cashier
- Expo

### Daily Reports

Opening and Closing shift reports can include:

- Date and shift
- Shift leader
- Number of employees working
- Daily notes
- Follow-up issues
- Inventory status
- Completed tasks
- Training information

### Report History

Previous reports can be reviewed to see inventory conditions, shift tasks, operational notes, and training information from earlier shifts.

## Technologies

- Python
- Streamlit
- JSON
- GitHub

## Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run ShiftFlow:

```bash
py -m streamlit run app.py
```

The application will open in your browser through Streamlit.

## Project Documentation

For a detailed explanation of the problem, design decisions, workflow, iterations, and lessons learned:

[View the ShiftFlow Design Process](DESIGN_PROCESS.md)

## Status

ShiftFlow is currently a working prototype and continues to be improved through usability and workflow testing.
