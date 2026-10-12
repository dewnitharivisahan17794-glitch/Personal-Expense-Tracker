# Personal Expense Tracker

# Personal Expense Tracker

A simple desktop **Personal Expense Tracker** built with **Python and Tkinter**.

This project allows users to record, manage, search, and track their daily expenses through a graphical user interface.

## 📌 Features

- Add new expenses
- View all expenses
- Update existing expenses
- Delete expenses
- Search expenses
- Calculate total expenses
- Calculate expenses by category
- Input validation
- Display expenses using `ttk.Treeview`
- Save and load data using JSON

## 🛠️ Technologies

- Python
- Tkinter
- ttk
- JSON

## 📋 Requirements

### Expense Information

The application should collect:

- Date
- Description
- Category
- Amount

### Categories

The application should provide the following categories:

- Food
- Transport
- Education
- Shopping
- Bills
- Other

## 🖥️ GUI Requirements

The main window should contain:

### Input Fields

- Date `Entry`
- Description `Entry`
- Category `Combobox`
- Amount `Entry`

### Buttons

- **Add Expense**
- **Update**
- **Delete**
- **Clear**
- **Search**

## 📊 Expense Table

Use `ttk.Treeview` to display the expenses.

| Date | Description | Category | Amount |
|---|---|---|---|
| 2026-10-05 | Lunch | Food | Rs. 450 |
| 2026-10-05 | Bus | Transport | Rs. 120 |

## 💰 Summary

The application should display the total amount spent.

Example:

```text
Total Expenses: Rs. 12,450.00
```

It should also display the total amount for each category.

```text
Food:       Rs. 5,200
Transport:  Rs. 2,100
Education:  Rs. 3,000
Other:      Rs. 2,150
```

## 🔄 CRUD Operations

### Create
Add a new expense using the input fields.

### Read
Display all saved expenses in the `Treeview`.

### Update
Select an expense and modify its information.

### Delete
Select an expense and remove it from the system.

### Search
Search for expenses based on relevant information such as description or category.

## ✅ Validation Requirements

- Date cannot be empty.
- Description cannot be empty.
- Category must be selected.
- Amount must be a valid number.
- Amount cannot be negative.
- Invalid input should display an appropriate error message using `messagebox`.

## 🖱️ Treeview Interaction

When the user selects an expense from the `Treeview`:

- The selected expense should load into the input fields.
- The user should be able to update or delete the selected expense.

## 💾 JSON Data Storage

The application should store expense data in a JSON file.

The application should:

- Load existing data when it starts.
- Save new expenses.
- Update the JSON file when an expense is modified.
- Update the JSON file when an expense is deleted.

## 🎯 Learning Goals

This project is designed to practice:

- Tkinter GUI development
- `Entry`
- `Button`
- `Combobox`
- `ttk.Treeview`
- `messagebox`
- Functions
- Lists and dictionaries
- CRUD operations
- Input validation
- JSON file handling
- Data filtering and searching
- Basic data calculations

## 🚀 Future Improvements

Possible future features:

- Monthly expense reports
- Date-range filtering
- Expense charts
- Pie chart for category spending
- Export data to CSV
- SQLite/MySQL database
- Dark mode
- User login system

## 📂 Project Status

**Status:** In Development 🚧

This project is part of a Python GUI project series created for practicing Python and Tkinter.

## 🤖 Project Attribution

The project idea and requirements were suggested by **ChatGPT** as part of a Python project learning exercise.

However, the **entire implementation and source code were independently designed and developed by me**.

ChatGPT was used only for:
- Project idea generation
- Requirements and specifications
- Guidance when needed
- Debugging and improvement suggestions

**All source code was written and implemented by me.**

my notes//

- Passkey is "17794"