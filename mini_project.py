import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import json
import os
from datetime import datetime,timedelta   
import pandas 
def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

def add_expense():
    clear_frame()
    global expense_entry, category_dropdown, date_entry
    # Creation enter expense label
    expense_label = tk.Label(window, text="Enter Expense:",
                             font=("Arial",12,"bold"),
                             bg="#BFBFF9", fg="#2C2C2C")
    expense_label.pack(pady=5)
    # Creation of expense entry
    expense_entry = tk.Entry(window, width=30)
    expense_entry.pack(pady=5,ipady=5)
    # Creation of category label
    label2 = tk.Label(window, text="Select Category:",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C")
    label2.pack(pady=5)
    # Types of categories to select
    categories = [
    "Food & Dining",
    "Groceries",
    "Transportation",
    "Fuel",
    "Shopping",
    "Entertainment",
    "Health & Fitness",
    "Medical",
    "Travel",
    "Education",
    "Bills & Utilities",
    "Rent",
    "Savings & Investments",
    "Gifts & Donations",
    "Personal Care",
    "Others"
    ]
    # Creation of category dropdown
    category_dropdown = ttk.Combobox(window, values=categories, width=27)
    category_dropdown.pack(pady=5,ipady=5)
    category_dropdown.set("Choose Category")  # default text
    # Creation of date label
    date_entry_label = tk.Label(window, text="Select Date:",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C")
    date_entry_label.pack(pady=5)
    # Creation of date entry
    date_entry = DateEntry(window, width=20, background="darkblue",
                       foreground="white", borderwidth=2, year=2025)
    date_entry.pack(pady=20 ,ipady=5)
    # Creation of Add expense button
    add_btn = tk.Button(window,
    text="Add Expense",
    command=lambda: added_successfully(expense_entry, category_dropdown, date_entry),
    bg="#0A66C2",
    fg="white",
    font=("Arial",12,"bold"))
    add_btn.pack(pady=10)
    # Creation of back button
    back_btn = tk.Button(window, text="⬅ Back", command=mainmenu,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def added_successfully(expense_entry, category_dropdown, date_entry):
    amount = expense_entry.get()
    category = category_dropdown.get()
    date = date_entry.get_date().strftime("%Y-%m-%d")  # YYYY-MM-DD
    month_key = date[:7]
    # Validation
    if not amount or category == "Choose Category":
        messagebox.showerror("Error", "Please enter all details!")
        return
    # Prepare expense dictionary
    expense_data = {
        "amount": float(amount),
        "category": category,
        "date": date
    }
    file_path = "expenses.json"
    # Load existing data or create new list
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    # If month not in data, create it
    if month_key not in data:
        data[month_key] = []

    # Append the expense to the month
    data[month_key].append(expense_data)
    # Save back to JSON
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    clear_frame()
    # Creation of added successfully label
    added_label = tk.Label(window, text="Expense Added Successfully!",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C")
    added_label.pack(pady=10)
    # Creation of Monthly Spending overview button
    monthly_spending_btn = tk.Button(window, text="Check Monthly Spending Overview", command=view_summary,bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    monthly_spending_btn.pack(pady=10)
    # Creation of back button
    back_btn = tk.Button(window, text="⬅ Back", command=mainmenu,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def view_summary():
    clear_frame()
    current_month = datetime.now().strftime("%Y-%m")  # e.g., "2025-08"
    file_path = "expenses.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = {}
    # Calculate total for current month
    if current_month in data:
        total = sum(expense["amount"] for expense in data[current_month])
    else:
        total = 0
    # Display on screen
    total_label = tk.Label(window, text=f"Total Spending This Month: ₹{total}", font=("Arial",14,"bold"), bg="#BFBFF9")
    total_label.pack(pady=10)
    # Creation of weekly Spending overview label
    weekly_spending_label = tk.Button(window, text="Weekly Spending Overview",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C",command=weekly_summary)
    weekly_spending_label.pack(pady=10,ipady=5)
    # Creation of Monthly Spending overview label
    monthly_spending_label = tk.Button(window, text="Monthly Spending Overview",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C",command=monthly_summary)
    monthly_spending_label.pack(pady=10,ipady=5)
    # Creation of yearly Spending overview label
    yearly_spending_label = tk.Button(window, text="Yearly Spending Overview",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C",command=yearly_summary)
    yearly_spending_label.pack(pady=10,ipady=5)
    # Creation of back button
    back_btn = tk.Button(window, text="⬅ Back", command=mainmenu,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def monthly_summary():
    clear_frame()
    current_month = datetime.now().strftime("%Y-%m")
    filepath = "expenses.json"
    if os.path.exists(filepath):
        with open(filepath,"r") as file :
            data = json.load(file)
    else:
        data = {}
    if current_month in data:
        total = sum(expense["amount"] for expense in data[current_month])
    else:
        total = 0
    total_label = tk.Label(window, text=f"Total Spending This Month: ₹{total}", font=("Arial",14,"bold"), bg="#BFBFF9")
    total_label.pack(pady=10)
    label2 = tk.Label(window, text="Select Category:",
                      font=("Arial",12,"bold"), bg="#BFBFF9", fg="#2C2C2C")
    label2.pack(pady=5)

    categories = [
        "Food & Dining", "Groceries", "Transportation", "Fuel",
        "Shopping", "Entertainment", "Health & Fitness", "Medical",
        "Travel", "Education", "Bills & Utilities", "Rent",
        "Savings & Investments", "Gifts & Donations",
        "Personal Care", "Others"
    ]

    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(window, values=categories,
                                     width=27, textvariable=selected_category)
    category_dropdown.pack(pady=5, ipady=5)
    category_dropdown.set("Choose Category")

    # Function to calculate category total
    def show_category_total():
        category = selected_category.get()
        if current_month in data:
            cat_total = sum(exp["amount"] for exp in data[current_month] if exp["category"] == category)
        else:
            cat_total = 0
        result_label.config(text=f"Total spent on {category}: ₹{cat_total}")

    # Button to check category spending
    check_btn = tk.Button(window, text="Check Category Spending",
                          command=show_category_total,
                          bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    check_btn.pack(pady=10)

    # Label to display result
    result_label = tk.Label(window, text="", font=("Arial",12,"bold"),
                            bg="#BFBFF9", fg="#2C2C2C")
    result_label.pack(pady=10)
    back_btn = tk.Button(window, text="⬅ Back", command=view_summary,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)
    
def weekly_summary():
    clear_frame()
    # to calculate weekly expense
    today = datetime.now().date()
    week_ago = today -  timedelta(days=7)
    filepath = "expenses.json"
    if os.path.exists(filepath):
        with open(filepath,"r") as file:
            data = json.load(file)
    weekly_total = 0
    for month_expenses in data.values():  # loop through all months
        for expense in month_expenses:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
            if week_ago <= expense_date <= today:
                weekly_total += expense["amount"]
    total_label = tk.Label(window, text=f"Total Spending This week: ₹{weekly_total}", font=("Arial",14,"bold"), bg="#BFBFF9")
    total_label.pack(pady=10)
    label2 = tk.Label(window, text="Select Category:",
                      font=("Arial",12,"bold"), bg="#BFBFF9", fg="#2C2C2C")
    label2.pack(pady=5)

    categories = [
        "Food & Dining", "Groceries", "Transportation", "Fuel",
        "Shopping", "Entertainment", "Health & Fitness", "Medical",
        "Travel", "Education", "Bills & Utilities", "Rent",
        "Savings & Investments", "Gifts & Donations",
        "Personal Care", "Others"
    ]

    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(window, values=categories,
                                     width=27, textvariable=selected_category)
    category_dropdown.pack(pady=5, ipady=5)
    category_dropdown.set("Choose Category")

    # Function to calculate category total for weekly range
    def show_category_total():
        category = selected_category.get()
        cat_total = 0
        for month_expenses in data.values():
            for expense in month_expenses:
                expense_date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
                if week_ago <= expense_date <= today and expense["category"] == category:
                    cat_total += expense["amount"]
        result_label.config(text=f"Total spent on {category} this week: ₹{cat_total}")

    # Button to check category spending
    check_btn = tk.Button(window, text="Check Category Spending",
                          command=show_category_total,
                          bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    check_btn.pack(pady=10)

    # Label to display result
    result_label = tk.Label(window, text="", font=("Arial",12,"bold"),
                            bg="#BFBFF9", fg="#2C2C2C")
    result_label.pack(pady=10)

    back_btn = tk.Button(window, text="⬅ Back", command=view_summary,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def yearly_summary():
    clear_frame()
    # to calculate yearly expense
    current_year = datetime.now().strftime("%Y")
    filepath = "expenses.json"
    if os.path.exists(filepath):
        with open(filepath,"r" ) as file :
            data = json.load(file)
    else:
        data = {}
    current_year = datetime.now().strftime("%Y")
    yearly_total = 0
    for month_key, month_expenses in data.items():
        if month_key.startswith(current_year):
            yearly_total += sum(expense["amount"] for expense in month_expenses)
    total_label = tk.Label(window, text=f"Total Spending This Year: ₹{yearly_total}", font=("Arial",14,"bold"), bg="#BFBFF9")
    total_label.pack(pady=10)
    back_btn = tk.Button(window, text="⬅ Back", command=view_summary,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)
    label2 = tk.Label(window, text="Select Category:",
                      font=("Arial",12,"bold"), bg="#BFBFF9", fg="#2C2C2C")
    label2.pack(pady=5)

    categories = [
        "Food & Dining", "Groceries", "Transportation", "Fuel",
        "Shopping", "Entertainment", "Health & Fitness", "Medical",
        "Travel", "Education", "Bills & Utilities", "Rent",
        "Savings & Investments", "Gifts & Donations",
        "Personal Care", "Others"
    ]

    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(window, values=categories,
                                     width=27, textvariable=selected_category)
    category_dropdown.pack(pady=5, ipady=5)
    category_dropdown.set("Choose Category")

    # Function to calculate category total for weekly range
    def show_category_total():
        category = selected_category.get()   # get category from dropdown
        cat_total = 0
        for month_key, month_expenses in data.items():
            if month_key.startswith(current_year):  # check same year
                for expense in month_expenses:
                    if expense["category"] == category:  # filter category
                        cat_total += expense["amount"]

        result_label.config(
            text=f"Total spent on {category} in {current_year}: ₹{cat_total}"
        )

    # Button to check category spending
    check_btn = tk.Button(window, text="Check Category Spending",
                          command=show_category_total,
                          bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    check_btn.pack(pady=10)

    # Label to display result
    result_label = tk.Label(window, text="", font=("Arial",12,"bold"),
                            bg="#BFBFF9", fg="#2C2C2C")
    result_label.pack(pady=10)
    
    back_btn = tk.Button(window, text="⬅ Back", command=view_summary,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def delete_expense():
    clear_frame()
    title = tk.Label(window,text = "DELETE EXPENSE",font=("Arial",18,"bold"),bg="#BFBFF9",fg="#2C2C2C")
    title.pack(pady=20)
    date_entry_label = tk.Label(window, text="Select Date:",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C")
    date_entry_label.pack(pady=5)
    # Creation of date entry
    date_entry = DateEntry(window, width=20, background="darkblue",
                       foreground="white", borderwidth=2, year=2025)
    date_entry.pack(pady=20 ,ipady=5)
    selected_date = date_entry.get()
    label2 = tk.Label(window, text="Select Category:",
                      font=("Arial",12,"bold"), bg="#BFBFF9", fg="#2C2C2C")
    label2.pack(pady=5)

    categories = [
        "Food & Dining", "Groceries", "Transportation", "Fuel",
        "Shopping", "Entertainment", "Health & Fitness", "Medical",
        "Travel", "Education", "Bills & Utilities", "Rent",
        "Savings & Investments", "Gifts & Donations",
        "Personal Care", "Others"
    ]
    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(window, values=categories,
                                     width=27, textvariable=selected_category)
    category_dropdown.pack(pady=5, ipady=5)
    category_dropdown.set("Choose Category")
    selected_delete_cat = category_dropdown.get()

    del_btn = tk.Button(
    window,
    text="Delete Expense",
    width=20,
    height=2,
    bg="#0A66C2",
    fg="white",
    font=("Arial", 12, "bold"),
    command=lambda: delete_expense_cat(date_entry.get(), category_dropdown.get())
    )
    del_btn.pack(pady=10)


    back_btn = tk.Button(window,text="⬅ Back",command=mainmenu,bg="#0A66C2",fg="white",font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def delete_expense_cat(selected_date, selected_delete_cat):
    clear_frame()
    filepath = "expenses.json"

    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
    else:
        data = {}

    expense_deleted = False  

    #  Convert selected_date from DateEntry (MM/DD/YY) → YYYY-MM-DD
    try:
        selected_date_obj = datetime.strptime(selected_date, "%m/%d/%y")
        selected_date_str = selected_date_obj.strftime("%Y-%m-%d")
        selected_month = selected_date_obj.strftime("%Y-%m")
    except ValueError:
        selected_date_str = selected_date
        selected_month = selected_date[:7]

    if selected_month in data:
        new_expenses = []
        for expense in data[selected_month]:
            #  Compare with correctly formatted date
            if not (expense["date"] == selected_date_str and expense["category"] == selected_delete_cat):
                new_expenses.append(expense)
            else:
                expense_deleted = True

        data[selected_month] = new_expenses

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

    # Show result
    msg = " Expense Deleted" if expense_deleted else " No Matching Expense Found"
    title = tk.Label(window, text=msg, font=("Arial",18,"bold"), bg="#BFBFF9", fg="#2C2C2C")
    title.pack(pady=20)

    view_summary_btn = tk.Button(window, text="View Summary", command=view_summary,
                                 bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    view_summary_btn.pack(pady=10)

    back_btn = tk.Button(window, text="⬅ Back", command=mainmenu,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def edit_expense():
    clear_frame()
    title = tk.Label(window,text = "EDIT EXPENSE",font=("Arial",18,"bold"),bg="#BFBFF9",fg="#2C2C2C")
    title.pack(pady=20)
    date_entry_label = tk.Label(window, text="Select Date:",font=("Arial",12,"bold"),bg="#BFBFF9",fg="#2C2C2C")
    date_entry_label.pack(pady=5)
    # Creation of date entry
    date_entry = DateEntry(window, width=20, background="darkblue",
                       foreground="white", borderwidth=2, year=2025)
    date_entry.pack(pady=20 ,ipady=5)
    label2 = tk.Label(window, text="Select Category:",
                      font=("Arial",12,"bold"), bg="#BFBFF9", fg="#2C2C2C")
    label2.pack(pady=5)

    categories = [
        "Food & Dining", "Groceries", "Transportation", "Fuel",
        "Shopping", "Entertainment", "Health & Fitness", "Medical",
        "Travel", "Education", "Bills & Utilities", "Rent",
        "Savings & Investments", "Gifts & Donations",
        "Personal Care", "Others"
    ]
    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(window, values=categories,
                                     width=27, textvariable=selected_category)
    category_dropdown.pack(pady=5, ipady=5)
    category_dropdown.set("Choose Category")

    expense_label = tk.Label(window, text="Enter Expense:",
                             font=("Arial",12,"bold"),
                             bg="#BFBFF9", fg="#2C2C2C")
    expense_label.pack(pady=5)
    # Creation of expense entry
    expense_entry = tk.Entry(window, width=30)
    expense_entry.pack(pady=5,ipady=5)

    edit_btn = tk.Button(
    window,
    text="Edit Expense",
    width=20,
    height=2,
    bg="#0A66C2",
    fg="white",
    font=("Arial", 12, "bold"),
    command=lambda: edit_expense_cat(date_entry.get(), category_dropdown.get(),expense_entry.get())
    )
    edit_btn.pack(pady=10)
    back_btn = tk.Button(window,text="⬅ Back",command=mainmenu,bg="#0A66C2",fg="white",font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def edit_expense_cat(selected_date,selected_delete_cat,edited_expense):
    clear_frame()
    filepath = "expenses.json"

    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
    else:
        data = {}

    expense_deleted = False  

    #  Convert selected_date from DateEntry (MM/DD/YY) → YYYY-MM-DD
    try:
        selected_date_obj = datetime.strptime(selected_date, "%m/%d/%y")
        selected_date_str = selected_date_obj.strftime("%Y-%m-%d")
        selected_month = selected_date_obj.strftime("%Y-%m")
    except ValueError:
        selected_date_str = selected_date
        selected_month = selected_date[:7]

    if selected_month in data:
        new_expenses = []
        for expense in data[selected_month]:
            if expense["date"] == selected_date_str and expense["category"] == selected_delete_cat:
                expense["amount"] = edited_expense
                expense_updated = True
            new_expenses.append(expense)

        data[selected_month] = new_expenses

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

    msg = " Expense Edited Successfully" if expense_updated else " No Expense Found To Edit"
    title = tk.Label(window, text=msg, font=("Arial",18,"bold"), bg="#BFBFF9", fg="#2C2C2C")
    title.pack(pady=20)

    view_summary_btn = tk.Button(window, text="View Summary", command=view_summary,
                                 bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    view_summary_btn.pack(pady=10)

    back_btn = tk.Button(window, text="⬅ Back", command=mainmenu,
                         bg="#0A66C2", fg="white", font=("Arial",12,"bold"))
    back_btn.pack(pady=10)

def expenses_list():
    clear_frame()
    title = tk.Label(window, text="Expenses list",
                     font=("Arial",18,"bold"),
                     bg="#BFBFF9", fg="#2C2C2C")
    title.pack(pady=20)
    filepath ="expenses.json"
    if os.path.exists(filepath):
        with open(filepath,"r") as file :
            data = json.load(file)
    else:
        data = {}
    
def mainmenu():
    clear_frame()
    title = tk.Label(window, text="EXPENSE MANAGER",
                     font=("Arial",18,"bold"),
                     bg="#BFBFF9", fg="#2C2C2C")
    title.pack(pady=20)

    btn1 = tk.Button(window, text="\u2795 Add Expense",
                     width=20, height=2, bg="#0A66C2", fg="white",
                     font=("Arial",12,"bold"), command=add_expense)
    btn1.pack(pady=10)

    btn2 = tk.Button(window, text="\u274C Delete Expense ",
                     width=20, height=2, bg="#0A66C2", fg="white",
                     font=("Arial",12,"bold"), command=delete_expense)
    btn2.pack(pady=10)

    btn3 = tk.Button(window, text="\u270E Edit Summary",
                     width=20, height=2, bg="#0A66C2", fg="white",
                     font=("Arial",12,"bold"), command=edit_expense)
    btn3.pack(pady=10)

    btn3 = tk.Button(window, text="\u270E Expenses List",
                     width=20, height=2, bg="#0A66C2", fg="white",
                     font=("Arial",12,"bold"), command=expenses_list)
    btn3.pack(pady=10)

    btn4 = tk.Button(window, text="\U0001F4CA Expense Summary",
                     width=20, height=2, bg="#0A66C2", fg="white",
                     font=("Arial",12,"bold"), command=view_summary)
    btn4.pack(pady=10)


    btn5 = tk.Button(window, text="\U0001F6AA Exit",
                     width=20, height=2, bg="#0A66C2", fg="white",
                     font=("Arial",12,"bold"), command=window.destroy)
    btn5.pack(pady=10)

window = tk.Tk()
window.title("Personal Expense Tracker")
window.geometry("500x500")
window.configure(bg="#BFBFF9")

mainmenu()
window.mainloop()
