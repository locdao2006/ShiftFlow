import streamlit as st
import json
import os
from datetime import date


DATA_FILE = "data.json"
DATA_VERSION = 5


# ==================================================
# INVENTORY CONFIGURATION
# Minimum levels are used internally.
# They are NOT displayed on the inventory page.
# ==================================================

INVENTORY_ITEMS = [

    # Minimum 5
    {"name": "Tapioca Pearls", "minimum": 5},
    {"name": "Brown Sugar", "minimum": 5},
    {"name": "Creme Brulee Powder", "minimum": 5},
    {"name": "Jelly Powder", "minimum": 5},
    {"name": "Oranges", "minimum": 5},
    {"name": "Mochi Powder", "minimum": 5},
    {"name": "Taro", "minimum": 5},

    # Minimum 3
    {"name": "Aloe Vera", "minimum": 3},
    {"name": "Tea Filters", "minimum": 3},
    {"name": "Dish Soap", "minimum": 3},
    {"name": "Floor Cleaner", "minimum": 3},

    # Minimum 15
    {"name": "Heavy Cream", "minimum": 15},
    {"name": "Organic Milk", "minimum": 15},
    {"name": "Oat Milk", "minimum": 15},
    {"name": "Almond Milk", "minimum": 15},

    # Syrups - Minimum 4
    {"name": "Lychee Syrup", "minimum": 4},
    {"name": "Strawberry Syrup", "minimum": 4},
    {"name": "Blueberry Syrup", "minimum": 4},
    {"name": "Mango Syrup", "minimum": 4},

    # Supplies - Minimum 4
    {"name": "Big Straws", "minimum": 4},
    {"name": "Small Straws", "minimum": 4},
    {"name": "16 oz Cups", "minimum": 4},
    {"name": "Small Cups", "minimum": 4},

    # Tea - Minimum 2
    {"name": "Green Tea", "minimum": 2},
    {"name": "Peach Oolong", "minimum": 2},
    {"name": "Royal No. 9 Tea", "minimum": 2}
]


# ==================================================
# SHIFT TASKS
# ==================================================

SHIFT_TASKS = [
    "Check inventory",
    "Prepare toppings",
    "Clean drink station",
    "Clean drains",
    "Take out trash",
    "Turn off air conditioning",
    "Organize supplies before closing",
    "Clean syrup and sugar area",
    "Sweep floor",
    "Mop floor",
    "Wipe down equipment and surfaces"
]


# ==================================================
# TRAINING STATIONS
# ==================================================

TRAINING_STATIONS = [
    "Prep",
    "Barista",
    "Cashier",
    "Expo"
]


# ==================================================
# SHIFT OPTIONS
# ==================================================

SHIFT_OPTIONS = [
    "Opening",
    "Closing"
]


# ==================================================
# DEFAULT DATA
# ==================================================

def create_default_data():

    return {
        "data_version": DATA_VERSION,
        "trainees": [],
        "inventory_reports": [],
        "task_reports": [],
        "daily_reports": []
    }


# ==================================================
# SAVE DATA
# ==================================================

def save_data(data):

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==================================================
# LOAD DATA
# ==================================================

def load_data():

    if not os.path.exists(DATA_FILE):

        new_data = create_default_data()

        save_data(new_data)

        return new_data

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            old_data = json.load(file)

    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):

        new_data = create_default_data()

        save_data(new_data)

        return new_data

    # Upgrade data version while keeping old information
    if old_data.get("data_version") != DATA_VERSION:

        new_data = create_default_data()

        if "trainees" in old_data:
            new_data["trainees"] = old_data["trainees"]

        if "inventory_reports" in old_data:
            new_data["inventory_reports"] = old_data[
                "inventory_reports"
            ]

        if "task_reports" in old_data:
            new_data["task_reports"] = old_data[
                "task_reports"
            ]

        if "daily_reports" in old_data:
            new_data["daily_reports"] = old_data[
                "daily_reports"
            ]

        save_data(new_data)

        return new_data

    # Make sure all sections exist
    if "trainees" not in old_data:
        old_data["trainees"] = []

    if "inventory_reports" not in old_data:
        old_data["inventory_reports"] = []

    if "task_reports" not in old_data:
        old_data["task_reports"] = []

    if "daily_reports" not in old_data:
        old_data["daily_reports"] = []

    return old_data


data = load_data()


# ==================================================
# HELPER FUNCTIONS
# ==================================================

def get_inventory_status(quantity, minimum):

    # 0 = completely out
    if quantity == 0:

        return "Out of Stock"

    # Below minimum = low
    elif quantity < minimum:

        return "Low Stock"

    # Minimum or higher = good
    else:

        return "In Stock"


def find_report(
    reports,
    report_date,
    shift
):

    for report in reports:

        if (
            report.get("date") == str(report_date)
            and
            report.get("shift") == shift
        ):

            return report

    return None


def upsert_report(
    reports,
    new_report
):

    for index, report in enumerate(reports):

        if (
            report.get("date") == new_report.get("date")
            and
            report.get("shift") == new_report.get("shift")
        ):

            reports[index] = new_report

            return "updated"

    reports.append(new_report)

    return "saved"


def set_quantity(key, value):

    st.session_state[key] = value


# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="ShiftFlow",
    page_icon="🧋",
    layout="wide"
)


# ==================================================
# HEADER
# ==================================================

st.title("🧋 ShiftFlow")

today = date.today()

formatted_today = today.strftime(
    "%A, %B %d, %Y"
)

st.write(
    "Daily operations and end-of-shift "
    "reporting for small food-service teams."
)

st.caption(formatted_today)


# ==================================================
# NAVIGATION
# ==================================================

(
    dashboard_tab,
    inventory_tab,
    tasks_tab,
    training_tab,
    report_tab,
    history_tab
) = st.tabs(
    [
        "Dashboard",
        "End-of-Day Inventory",
        "Shift Tasks",
        "Training Tracker",
        "Daily Report",
        "Report History"
    ]
)


# ==================================================
# DASHBOARD
# ==================================================

with dashboard_tab:

    st.header("Today's Dashboard")

    st.subheader(formatted_today)

    latest_inventory = None

    if len(data["inventory_reports"]) > 0:

        latest_inventory = data[
            "inventory_reports"
        ][-1]

    latest_tasks = None

    if len(data["task_reports"]) > 0:

        latest_tasks = data[
            "task_reports"
        ][-1]

    in_stock_count = 0
    low_stock_count = 0
    out_stock_count = 0

    if latest_inventory:

        for item in latest_inventory["items"]:

            if item["status"] == "In Stock":

                in_stock_count += 1

            elif item["status"] == "Low Stock":

                low_stock_count += 1

            elif item["status"] == "Out of Stock":

                out_stock_count += 1

    completed_tasks = 0

    total_tasks = len(SHIFT_TASKS)

    if latest_tasks:

        completed_tasks = latest_tasks.get(
            "completed_count",
            0
        )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "In Stock",
        in_stock_count
    )

    col2.metric(
        "Low Stock",
        low_stock_count
    )

    col3.metric(
        "Out of Stock",
        out_stock_count
    )

    col4.metric(
        "Tasks Completed",
        f"{completed_tasks}/{total_tasks}"
    )

    st.divider()

    # --------------------------------------------------
    # INVENTORY ALERTS
    # --------------------------------------------------

    st.subheader(
        "Items Needing Attention"
    )

    if latest_inventory is None:

        st.info(
            "No end-of-day inventory "
            "has been submitted yet."
        )

    else:

        st.caption(
            f"Inventory from "
            f"{latest_inventory['date']} "
            f"— {latest_inventory['shift']} Shift"
        )

        needs_attention = False

        for item in latest_inventory["items"]:

            if item["status"] == "Out of Stock":

                needs_attention = True

                st.error(
                    f"🚨 {item['name']} — "
                    f"OUT OF STOCK"
                )

            elif item["status"] == "Low Stock":

                needs_attention = True

                st.warning(
                    f"⚠️ {item['name']} — "
                    f"{item['quantity']} remaining"
                )

        if not needs_attention:

            st.success(
                "Everything is currently in stock."
            )

    st.divider()

    # --------------------------------------------------
    # EMPLOYEE TRAINING
    # --------------------------------------------------

    st.subheader(
        "Employee Training"
    )

    if len(data["trainees"]) == 0:

        st.info(
            "No employees currently in training."
        )

    else:

        for trainee in data["trainees"]:

            st.write(
                f"**{trainee['name']}** — "
                f"{trainee['station']} — "
                f"{trainee['progress']}%"
            )


# ==================================================
# END-OF-DAY INVENTORY
# ==================================================

with inventory_tab:

    st.header(
        "End-of-Day Inventory"
    )

    st.write(
        "Enter the quantity remaining "
        "at the end of the shift."
    )

    st.caption(
        "Use a quick quantity button, "
        "then use + / - if you need an exact amount."
    )

    # --------------------------------------------------
    # DATE AND SHIFT
    # --------------------------------------------------

    inventory_date = st.date_input(
        "Inventory Date",
        value=date.today(),
        key="inventory_date"
    )

    inventory_shift = st.selectbox(
        "Shift",
        SHIFT_OPTIONS,
        key="inventory_shift"
    )

    existing_inventory_report = find_report(
        data["inventory_reports"],
        inventory_date,
        inventory_shift
    )

    existing_quantities = {}

    if existing_inventory_report:

        for item in existing_inventory_report["items"]:

            existing_quantities[
                item["name"]
            ] = item["quantity"]

        st.info(
            "An inventory report already exists "
            "for this date and shift. "
            "Saving again will update it."
        )

    st.divider()

    inventory_values = {}

    # ==================================================
    # INVENTORY LIST
    # ==================================================

    for index, item in enumerate(
        INVENTORY_ITEMS
    ):

        quantity_key = (
            f"inventory_quantity_"
            f"{inventory_date}_"
            f"{inventory_shift}_"
            f"{index}"
        )

        default_quantity = existing_quantities.get(
            item["name"],
            0
        )

        if quantity_key not in st.session_state:

            st.session_state[
                quantity_key
            ] = int(default_quantity)

        # --------------------------------------------------
        # ITEM NAME
        # --------------------------------------------------

        st.markdown(
            f"### {item['name']}"
        )

        # --------------------------------------------------
        # QUICK QUANTITY BUTTONS
        # --------------------------------------------------

        st.caption(
            "Quick quantity"
        )

        q0, q5, q10, q15, q20 = st.columns(5)

        q0.button(
            "0",
            key=(
                f"quick_0_"
                f"{inventory_date}_"
                f"{inventory_shift}_"
                f"{index}"
            ),
            on_click=set_quantity,
            args=(
                quantity_key,
                0
            ),
            use_container_width=True
        )

        q5.button(
            "5",
            key=(
                f"quick_5_"
                f"{inventory_date}_"
                f"{inventory_shift}_"
                f"{index}"
            ),
            on_click=set_quantity,
            args=(
                quantity_key,
                5
            ),
            use_container_width=True
        )

        q10.button(
            "10",
            key=(
                f"quick_10_"
                f"{inventory_date}_"
                f"{inventory_shift}_"
                f"{index}"
            ),
            on_click=set_quantity,
            args=(
                quantity_key,
                10
            ),
            use_container_width=True
        )

        q15.button(
            "15",
            key=(
                f"quick_15_"
                f"{inventory_date}_"
                f"{inventory_shift}_"
                f"{index}"
            ),
            on_click=set_quantity,
            args=(
                quantity_key,
                15
            ),
            use_container_width=True
        )

        q20.button(
            "20",
            key=(
                f"quick_20_"
                f"{inventory_date}_"
                f"{inventory_shift}_"
                f"{index}"
            ),
            on_click=set_quantity,
            args=(
                quantity_key,
                20
            ),
            use_container_width=True
        )

        # --------------------------------------------------
        # EXACT QUANTITY
        # --------------------------------------------------

        quantity = st.number_input(
            "Remaining Quantity",
            min_value=0,
            step=1,
            key=quantity_key
        )

        inventory_values[
            item["name"]
        ] = quantity

        # --------------------------------------------------
        # STATUS
        # --------------------------------------------------

        status = get_inventory_status(
            quantity,
            item["minimum"]
        )

        if status == "Out of Stock":

            st.error(
                f"🚨 OUT OF STOCK — "
                f"{item['name']} has 0 remaining."
            )

        elif status == "Low Stock":

            st.warning(
                f"⚠️ LOW STOCK — "
                f"{quantity} remaining."
            )

        else:

            st.success(
                f"✅ IN STOCK — "
                f"{quantity} remaining."
            )

        st.divider()

    # ==================================================
    # SAVE INVENTORY
    # ==================================================

    if st.button(
        "Save End-of-Day Inventory",
        type="primary",
        use_container_width=True
    ):

        inventory_snapshot = []

        for item in INVENTORY_ITEMS:

            quantity = int(
                inventory_values[
                    item["name"]
                ]
            )

            status = get_inventory_status(
                quantity,
                item["minimum"]
            )

            inventory_snapshot.append(
                {
                    "name":
                        item["name"],

                    "quantity":
                        quantity,

                    "minimum":
                        item["minimum"],

                    "status":
                        status
                }
            )

        new_inventory_report = {

            "date":
                str(inventory_date),

            "shift":
                inventory_shift,

            "items":
                inventory_snapshot
        }

        result = upsert_report(
            data["inventory_reports"],
            new_inventory_report
        )

        save_data(data)

        if result == "saved":

            st.success(
                "End-of-day inventory saved!"
            )

        else:

            st.success(
                "Inventory report updated!"
            )

        st.rerun()


# ==================================================
# SHIFT TASKS
# ==================================================

with tasks_tab:

    st.header(
        "Shift Tasks"
    )

    st.write(
        "Complete the checklist before "
        "ending the shift."
    )

    task_date = st.date_input(
        "Task Date",
        value=date.today(),
        key="task_date"
    )

    task_shift = st.selectbox(
        "Shift",
        SHIFT_OPTIONS,
        key="task_shift"
    )

    existing_task_report = find_report(
        data["task_reports"],
        task_date,
        task_shift
    )

    previous_tasks = {}

    if existing_task_report:

        for task in existing_task_report["tasks"]:

            previous_tasks[
                task["task"]
            ] = task["done"]

        st.info(
            "A task report already exists "
            "for this shift. Saving again "
            "will update it."
        )

    st.divider()

    task_values = {}

    for index, task_name in enumerate(
        SHIFT_TASKS
    ):

        default_done = previous_tasks.get(
            task_name,
            False
        )

        checked = st.checkbox(
            task_name,
            value=default_done,
            key=(
                f"shift_task_"
                f"{task_date}_"
                f"{task_shift}_"
                f"{index}"
            )
        )

        task_values[
            task_name
        ] = checked

    st.divider()

    completed_preview = sum(
        task_values.values()
    )

    st.write(
        f"**Completed:** "
        f"{completed_preview}/"
        f"{len(SHIFT_TASKS)}"
    )

    if st.button(
        "Save Shift Tasks",
        type="primary"
    ):

        task_snapshot = []

        completed_count = 0

        for task_name in SHIFT_TASKS:

            done = task_values[
                task_name
            ]

            if done:

                completed_count += 1

            task_snapshot.append(
                {
                    "task":
                        task_name,

                    "done":
                        done
                }
            )

        new_task_report = {

            "date":
                str(task_date),

            "shift":
                task_shift,

            "tasks":
                task_snapshot,

            "completed_count":
                completed_count
        }

        result = upsert_report(
            data["task_reports"],
            new_task_report
        )

        save_data(data)

        if result == "saved":

            st.success(
                "Shift tasks saved!"
            )

        else:

            st.success(
                "Shift tasks updated!"
            )

        st.rerun()


# ==================================================
# TRAINING TRACKER
# ==================================================

with training_tab:

    st.header(
        "Training Tracker"
    )

    # --------------------------------------------------
    # CURRENT TRAINEES
    # --------------------------------------------------

    if len(data["trainees"]) == 0:

        st.info(
            "No employees currently "
            "in training."
        )

    else:

        for index, trainee in enumerate(
            data["trainees"]
        ):

            col1, col2, col3, col4 = (
                st.columns(
                    [3, 3, 3, 1]
                )
            )

            col1.write(
                f"**{trainee['name']}**"
            )

            col2.write(
                trainee["station"]
            )

            col3.progress(
                trainee["progress"] / 100
            )

            col3.caption(
                f"{trainee['progress']}%"
            )

            if col4.button(
                "Delete",
                key=(
                    f"delete_trainee_"
                    f"{index}"
                )
            ):

                data[
                    "trainees"
                ].pop(index)

                save_data(data)

                st.rerun()

    st.divider()

    # --------------------------------------------------
    # ADD EMPLOYEE TRAINING
    # --------------------------------------------------

    st.subheader(
        "Add Employee Training"
    )

    with st.form(
        "add_training_form"
    ):

        employee_name = st.text_input(
            "Employee Name"
        )

        employee_station = st.selectbox(
            "Station",
            TRAINING_STATIONS
        )

        employee_progress = st.slider(
            "Progress",
            min_value=0,
            max_value=100,
            value=0,
            step=10
        )

        add_employee = (
            st.form_submit_button(
                "Add Employee"
            )
        )

    if add_employee:

        if employee_name.strip() == "":

            st.error(
                "Please enter an employee name."
            )

        else:

            data["trainees"].append(
                {
                    "name":
                        employee_name.strip(),

                    "station":
                        employee_station,

                    "progress":
                        employee_progress
                }
            )

            save_data(data)

            st.success(
                "Employee added!"
            )

            st.rerun()

    # --------------------------------------------------
    # UPDATE TRAINING
    # --------------------------------------------------

    if len(data["trainees"]) > 0:

        st.divider()

        st.subheader(
            "Update Training"
        )

        trainee_names = [

            trainee["name"]

            for trainee
            in data["trainees"]
        ]

        selected_employee = st.selectbox(
            "Employee",
            trainee_names,
            key="update_employee"
        )

        selected_station = st.selectbox(
            "Station",
            TRAINING_STATIONS,
            key="update_station"
        )

        updated_progress = st.slider(
            "New Progress",
            min_value=0,
            max_value=100,
            value=50,
            step=10,
            key="updated_progress"
        )

        if st.button(
            "Update Training"
        ):

            for trainee in data["trainees"]:

                if (
                    trainee["name"]
                    == selected_employee
                ):

                    trainee[
                        "station"
                    ] = selected_station

                    trainee[
                        "progress"
                    ] = updated_progress

            save_data(data)

            st.success(
                "Training updated!"
            )

            st.rerun()


# ==================================================
# DAILY REPORT
# ==================================================

with report_tab:

    st.header(
        "Daily Shift Report"
    )

    st.write(
        "Complete inventory and shift tasks "
        "first, then save the final daily report."
    )

    report_date = st.date_input(
        "Report Date",
        value=date.today(),
        key="daily_report_date"
    )

    report_shift = st.selectbox(
        "Shift",
        SHIFT_OPTIONS,
        key="daily_report_shift"
    )

    # --------------------------------------------------
    # MATCH INVENTORY + TASKS
    # --------------------------------------------------

    matching_inventory = find_report(
        data["inventory_reports"],
        report_date,
        report_shift
    )

    matching_tasks = find_report(
        data["task_reports"],
        report_date,
        report_shift
    )

    # --------------------------------------------------
    # INVENTORY SUMMARY
    # --------------------------------------------------

    st.subheader(
        "Inventory Summary"
    )

    if matching_inventory is None:

        st.warning(
            "Inventory has not been "
            "submitted for this shift yet."
        )

    else:

        in_count = 0
        low_count = 0
        out_count = 0

        for item in matching_inventory[
            "items"
        ]:

            if item["status"] == "In Stock":

                in_count += 1

            elif item["status"] == "Low Stock":

                low_count += 1

            else:

                out_count += 1

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "In Stock",
            in_count
        )

        c2.metric(
            "Low Stock",
            low_count
        )

        c3.metric(
            "Out of Stock",
            out_count
        )

    # --------------------------------------------------
    # TASK SUMMARY
    # --------------------------------------------------

    st.subheader(
        "Task Summary"
    )

    if matching_tasks is None:

        st.warning(
            "Shift tasks have not been "
            "submitted yet."
        )

    else:

        st.write(
            f"**Completed:** "
            f"{matching_tasks['completed_count']}"
            f"/{len(SHIFT_TASKS)}"
        )

    st.divider()

    # --------------------------------------------------
    # EXISTING DAILY REPORT
    # --------------------------------------------------

    existing_daily_report = find_report(
        data["daily_reports"],
        report_date,
        report_shift
    )

    existing_leader = ""
    existing_staff = 1
    existing_notes = ""
    existing_issues = ""

    if existing_daily_report:

        existing_leader = (
            existing_daily_report.get(
                "shift_leader",
                ""
            )
        )

        existing_staff = (
            existing_daily_report.get(
                "staff_count",
                1
            )
        )

        existing_notes = (
            existing_daily_report.get(
                "notes",
                ""
            )
        )

        existing_issues = (
            existing_daily_report.get(
                "issues",
                ""
            )
        )

        st.info(
            "A daily report already exists "
            "for this shift. Saving again "
            "will update it."
        )

    shift_leader = st.text_input(
        "Shift Leader",
        value=existing_leader
    )

    staff_count = st.number_input(
        "Number of Staff Working",
        min_value=1,
        value=int(existing_staff),
        step=1
    )

    notes = st.text_area(
        "Daily Notes",
        value=existing_notes,
        placeholder=(
            "Example: Busy from 6 PM to 8 PM. "
            "Team handled the rush well."
        )
    )

    issues = st.text_area(
        "Issues / Follow Up",
        value=existing_issues,
        placeholder=(
            "Example: Oat milk is low. "
            "Need to reorder tomorrow."
        )
    )

    st.divider()

    # --------------------------------------------------
    # SAVE FINAL DAILY REPORT
    # --------------------------------------------------

    if st.button(
        "Save Final Daily Report",
        type="primary"
    ):

        if shift_leader.strip() == "":

            st.error(
                "Please enter the "
                "shift leader's name."
            )

        else:

            inventory_snapshot = []

            if matching_inventory:

                inventory_snapshot = (
                    matching_inventory[
                        "items"
                    ]
                )

            task_snapshot = []

            if matching_tasks:

                task_snapshot = (
                    matching_tasks[
                        "tasks"
                    ]
                )

            training_snapshot = []

            for trainee in data["trainees"]:

                training_snapshot.append(
                    {
                        "name":
                            trainee["name"],

                        "station":
                            trainee["station"],

                        "progress":
                            trainee["progress"]
                    }
                )

            new_daily_report = {

                "date":
                    str(report_date),

                "shift":
                    report_shift,

                "shift_leader":
                    shift_leader.strip(),

                "staff_count":
                    int(staff_count),

                "notes":
                    notes.strip(),

                "issues":
                    issues.strip(),

                "inventory":
                    inventory_snapshot,

                "tasks":
                    task_snapshot,

                "training":
                    training_snapshot
            }

            result = upsert_report(
                data["daily_reports"],
                new_daily_report
            )

            save_data(data)

            if result == "saved":

                st.success(
                    "Final daily report saved!"
                )

            else:

                st.success(
                    "Daily report updated!"
                )

            st.rerun()


# ==================================================
# REPORT HISTORY
# ==================================================

with history_tab:

    st.header(
        "Report History"
    )

    if len(
        data["daily_reports"]
    ) == 0:

        st.info(
            "No final daily reports "
            "have been saved yet."
        )

    else:

        reports_reversed = list(
            reversed(
                data["daily_reports"]
            )
        )

        for report in reports_reversed:

            title = (
                f"{report.get('date', 'Unknown')} "
                f"— "
                f"{report.get('shift', 'Shift')}"
            )

            with st.expander(title):

                st.write(
                    f"**Shift Leader:** "
                    f"{report.get('shift_leader', 'N/A')}"
                )

                st.write(
                    f"**Staff Working:** "
                    f"{report.get('staff_count', 'N/A')}"
                )

                st.write(
                    f"**Daily Notes:** "
                    f"{report.get('notes', '') or 'None'}"
                )

                st.write(
                    f"**Issues / Follow Up:** "
                    f"{report.get('issues', '') or 'None'}"
                )

                st.divider()

                # --------------------------------------------------
                # INVENTORY HISTORY
                # --------------------------------------------------

                st.subheader(
                    "Inventory"
                )

                report_inventory = (
                    report.get(
                        "inventory",
                        []
                    )
                )

                if len(report_inventory) == 0:

                    st.write(
                        "No inventory snapshot "
                        "was saved with this report."
                    )

                else:

                    for item in report_inventory:

                        status = item.get(
                            "status",
                            ""
                        )

                        if status == "Out of Stock":

                            st.error(
                                f"🚨 {item['name']} — "
                                f"{item['quantity']} — "
                                f"Out of Stock"
                            )

                        elif status == "Low Stock":

                            st.warning(
                                f"⚠️ {item['name']} — "
                                f"{item['quantity']} — "
                                f"Low Stock"
                            )

                        else:

                            st.write(
                                f"✅ {item['name']} — "
                                f"{item['quantity']} — "
                                f"In Stock"
                            )

                st.divider()

                # --------------------------------------------------
                # TASK HISTORY
                # --------------------------------------------------

                st.subheader(
                    "Shift Tasks"
                )

                report_tasks = (
                    report.get(
                        "tasks",
                        []
                    )
                )

                if len(report_tasks) == 0:

                    st.write(
                        "No task snapshot "
                        "was saved."
                    )

                else:

                    for task in report_tasks:

                        if task.get(
                            "done",
                            False
                        ):

                            st.write(
                                f"✅ {task['task']}"
                            )

                        else:

                            st.write(
                                f"⬜ {task['task']}"
                            )

                st.divider()

                # --------------------------------------------------
                # TRAINING HISTORY
                # --------------------------------------------------

                st.subheader(
                    "Employee Training"
                )

                training_history = (
                    report.get(
                        "training",
                        []
                    )
                )

                if len(training_history) == 0:

                    st.write(
                        "No employee training "
                        "recorded."
                    )

                else:

                    for trainee in training_history:

                        st.write(
                            f"**{trainee['name']}** "
                            f"— {trainee['station']} "
                            f"— {trainee['progress']}%"
                        )