# ShiftFlow Design Process

## Background

ShiftFlow began as a self-directed project inspired by operational challenges I observed while working in a fast-paced food-service environment.

During busy shifts, employees and shift leaders need to keep track of multiple types of information at the same time, including inventory levels, cleaning responsibilities, employee training progress, and notes that need to be communicated to the next shift.

I wanted to explore how a simple information system could make these responsibilities easier to organize and review.

## Problem

Important operational information is often spread across memory, handwritten notes, verbal communication, or separate checklists.

This creates several potential problems:

- Inventory shortages may not be noticed until the next shift.
- Closing responsibilities can be missed.
- Training progress may be difficult to track consistently.
- Important information may not be communicated clearly between shifts.

ShiftFlow was designed to centralize this information into one workflow.

## Design Goals

The main goals of the project were:

- Make end-of-shift reporting quick and simple.
- Reduce the amount of information employees need to remember.
- Clearly identify low-stock and out-of-stock items.
- Create a consistent checklist for shift responsibilities.
- Track employee progress across different work stations.
- Preserve shift information so it can be reviewed later.

## Inventory Design

The inventory section lists commonly used food-service items and allows users to enter the quantity remaining at the end of a shift.

To reduce repetitive typing, I added quick quantity buttons for:

- 0
- 5
- 10
- 15
- 20

Users can then adjust the exact quantity using the number input control.

Each item has an internal minimum quantity. The application automatically determines its status:

- Quantity = 0 → Out of Stock
- Quantity below the minimum → Low Stock
- Quantity equal to or above the minimum → In Stock

This allows users to identify inventory problems without manually comparing each value.

## Shift Workflow

The intended workflow is:

1. Complete the end-of-day inventory count.
2. Complete the shift task checklist.
3. Update employee training progress if needed.
4. Add notes and follow-up issues.
5. Save the final shift report.
6. Review previous reports through Report History.

## Training Tracker

The Training Tracker supports four work stations:

- Prep
- Barista
- Cashier
- Expo

Each employee can be assigned a station and a percentage representing their training progress.

## Iteration

The project changed several times during development.

For example, the first inventory design focused on adding and subtracting stock throughout the day. I later redesigned it as an end-of-shift reporting system because that workflow better matched the real problem I wanted to address.

I also simplified the inventory interface by adding quick quantity buttons and removing unnecessary minimum-level information from the visible interface while keeping the inventory rules in the program logic.

These changes helped make the interface faster and easier to use.

## What I Learned

This project helped me practice more than programming alone.

I learned how to:

- Translate a workplace problem into software requirements.
- Design around a user's workflow.
- Organize information across multiple application sections.
- Use Python data structures and conditional logic.
- Persist structured data using JSON.
- Build interactive interfaces using Streamlit.
- Revise an interface based on usability considerations.
- Think about how technology supports communication and organizational processes.

## Future Improvements

Future versions could include:

- User authentication
- Manager and employee permission levels
- Cloud database storage
- Inventory trend charts
- Reorder recommendations
- Employee-specific training history
- Mobile interface improvements
- Exportable reports
- Notifications for low-stock items
- Multiple store locations

## Interface Screenshots

The following screenshots show the current ShiftFlow prototype and its main workflows.

### Dashboard

The dashboard provides a quick overview of inventory status, completed shift tasks, and other information that may need attention.

![ShiftFlow Dashboard](screenshots/dashboard.png)

### End-of-Day Inventory

The inventory interface allows users to quickly enter the amount of each item remaining at the end of a shift.

![End-of-Day Inventory](screenshots/inventory1.png)

Quick quantity buttons reduce repetitive data entry and allow common values to be selected with one click.

![Inventory Quantity Entry](screenshots/inventory2.png)

The interface automatically displays whether each item is In Stock, Low Stock, or Out of Stock.

![Inventory Status](screenshots/inventory3.png)

### Shift Tasks

The Shift Tasks section provides a consistent checklist for responsibilities that need to be completed during a shift.

![Shift Tasks](screenshots/shifttask1.png)

Task completion is tracked and can be saved for each Opening or Closing shift.

![Shift Task Checklist](screenshots/shifttask2.png)

### Training Tracker

The Training Tracker allows employee progress to be recorded across Prep, Barista, Cashier, and Expo stations.

![Training Tracker](screenshots/trainingtracker1.png)

Training percentages can be updated as employees develop their skills at each station.

![Employee Training Progress](screenshots/trainingtracker2.png)

### Daily Report

The Daily Report combines shift information, inventory results, task completion, notes, and follow-up issues into one record.

![Daily Report](screenshots/dailyreport1.png)

Inventory and task summaries allow the shift leader to review the current shift before saving the final report.

![Daily Report Summary](screenshots/dailyreport2.png)

### Report History

Report History allows previous shift reports to be reviewed later, preserving information about inventory, tasks, training, and operational notes.

![Report History](screenshots/reporthistory.png)
