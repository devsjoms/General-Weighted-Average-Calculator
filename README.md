# GWA Calculator

A simple and modern **General Weighted Average (GWA) Calculator** built with **Python** and **CustomTkinter**.

The application allows students to enter their subjects, units, and grades, then automatically calculates their weighted GWA.

## Features

* Modern desktop UI using CustomTkinter
* Dark Mode and Light Mode
* Supports up to **12 subjects**
* Dynamic subject input fields
* Course name, units, and grade inputs
* Input validation and error handling
* Weighted GWA calculation
* Total subjects and total units display
* Scrollable subject list
* Calculate Again / Reset functionality
* Easy dependency installation using `requirements.txt`

## Technologies Used

* **Python**
* **CustomTkinter**
* **Tkinter**

## Project Structure

```text
GWA-Calculator/
│
├── main.py
├── requirements.txt
├── setup.bat
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/devsjoms/gwa-calculator.git
```

### 2. Open the project folder

```bash
cd gwa-calculator
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```
## How to Use

### Step 1 — Enter Number of Subjects

Enter the number of subjects you want to calculate.

The application supports:

```text
1 - 12 subjects
```

### Step 2 — Enter Subject Information

For each subject, enter:

* Course Name
* Number of Units
* Grade

Example:

```text
Course Name: IT101
Units: 3
Grade: 1.50
```

### Step 3 — Calculate

Click **Calculate GWA**.

The application calculates the weighted average using:

```text
GWA = Σ(Grade × Units) / Σ(Units)
```

### Example

Given:

| Course | Units | Grade |
| ------ | ----: | ----: |
| IT101  |     3 |  1.50 |
| IT102  |     3 |  1.75 |
| IT103  |     3 |  2.00 |

The application calculates the GWA based on the total weighted grades and total units.

## Input Validation

The application checks for invalid inputs such as:

* Empty fields
* Invalid number of subjects
* More than 12 subjects
* Zero or negative units
* Invalid grade values
* Non-numeric units
* Non-numeric grades

Grades must be within:

```text
1.00 - 5.00
```

## Requirements

Python 3.9 or later is recommended.

Install the required dependency with:

```bash
pip install -r requirements.txt
```

## Requirements File

The project uses `requirements.txt` to manage external Python dependencies.

```text
customtkinter
```

## Future Improvements

Possible improvements for future versions:

* Save calculation history
* Export results to PDF
* Export results to CSV
* Add semester management
* Add GPA/GWA history
* Add grade interpretation
* Add customizable grading scales
* Add application icon
* Package the application as a standalone `.exe`

## Purpose

This project was created as a learning project to practice:

* Python functions
* Variables and data types
* Loops
* Conditional statements
* Exception handling
* Lists
* User input validation
* GUI development
* Basic application structure

## Author

**Jomar Naval**

Aspiring Web Developer and Software Engineer

Built with Python and CustomTkinter.
