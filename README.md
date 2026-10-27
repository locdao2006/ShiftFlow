# ShiftFlow

ShiftFlow is a self-directed web application designed to help small food-service teams organize and document daily operations.

The project was inspired by challenges I observed while working in a fast-paced food-service environment, where shift leaders often need to track inventory, complete opening and closing tasks, monitor employee training, and communicate important information between shifts.

ShiftFlow brings these responsibilities into one centralized system.

## Features

### End-of-Day Inventory

Employees can enter the remaining quantity of each inventory item at the end of a shift.

To make inventory entry faster, the application includes quick-select quantity buttons such as:

- 0
- 5
- 10
- 15
- 20

Exact quantities can also be adjusted manually.

The system automatically classifies each item as:

- ✅ In Stock
- ⚠️ Low Stock
- 🚨 Out of Stock

Inventory thresholds vary depending on the type of product and expected operational needs.

### Shift Task Checklist

ShiftFlow provides a checklist for important opening and closing responsibilities, including:

- Checking inventory
- Preparing toppings
- Cleaning drink stations
- Cleaning drains
- Taking out trash
- Organizing supplies
- Cleaning syrup and sugar areas
- Sweeping and mopping floors
- Turning off equipment
- Wiping down work surfaces

Task completion can be saved separately for each shift.

### Employee Training Tracker

Managers or shift leaders can track employee training progress across four main stations:

- Prep
- Barista
- Cashier
- Expo

Each employee can be assigned a station and a training completion percentage.

### Daily Shift Reports

Shift leaders can create reports for Opening and Closing shifts.

Each report can include:

- Date
- Shift
- Shift leader
- Number of employees working
- Daily notes
- Issues requiring follow-up
- Inventory status
- Completed shift tasks
- Employee training progress

If a report already exists for the same date and shift, ShiftFlow updates the existing report instead of creating a duplicate.

### Report History

Saved reports can be reviewed later to understand what happened during previous shifts.

The report history includes:

- Inventory quantities and status
- Completed and incomplete tasks
- Daily operational notes
- Follow-up issues
- Employee training progress

## Inventory Logic

ShiftFlow automatically determines inventory status using predefined minimum levels.

For example, if the minimum quantity for Tapioca Pearls is 5:

- Quantity = 0 → Out of Stock
- Quantity = 1–4 → Low Stock
- Quantity ≥ 5 → In Stock

This logic allows users to quickly identify items that may need to be reordered or restocked.

## Technologies Used

- Python
- Streamlit
- JSON
- GitHub

## Project Purpose

I created ShiftFlow as a way to apply programming to a real operational problem.

Rather than building a program only for technical practice, I wanted to design a tool around how people actually work in a fast-paced environment.

The project combines:

- User-centered design
- Information organization
- Workflow improvement
- Interactive interface design
- Data storage
- Business logic
- Operational problem solving

Building ShiftFlow also helped me explore my interest in Informatics, especially how technology can support people, communication, and organizational processes.

## What I Learned

Through this project, I gained more experience with:

- Designing software around user needs
- Building interactive applications with Streamlit
- Using Python functions, lists, dictionaries, and conditional logic
- Saving and retrieving structured information with JSON
- Creating reusable application components
- Designing inventory status rules
- Managing information across multiple shifts
- Improving an application through repeated testing and revision

## Future Improvements

Possible future improvements include:

- User login and manager permissions
- Cloud database storage
- Mobile-friendly interface improvements
- Inventory usage trends over time
- Automatic reorder recommendations
- Employee-specific training history
- Charts and operational analytics
- Notifications for low-stock items
- Exportable daily reports
- Multi-location support

## Running the Project

Install the required package:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
py -m streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Project Status

ShiftFlow is currently a working prototype and is continuing to be improved based on usability, workflow, and feature testing.
