# Mouse Database Application

#### Vedio Demo: https://youtu.be/OhXtMd5Aq8w

Title: Mouse Sheet Manager
Name: Hsuan-Ming Chi
GitHub: AlanChi0720
Location: New Jersey, USA
Date: 03/11/2024

I am a lab manager and interested in programmning so I decided to build up this application for my daily work use.

This is a Python application that allows users to manage mouse data in a SQLite database. The application provides a graphical user interface (GUI) built with Tkinter, where users can input cage numbers, mouse numbers, and dates of birth for mice.

## Features

- Add new mouse data to the database
- View the entire database in a Pandas DataFrame
- Delete data by providing either the cage number or mouse number

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pandas
- SQLite3 (included with Python)

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:
```
pip install pandas
```

## Usage

1. Run the `mouse_app.py` file.
2. The Mouse Database Application GUI will open.
3. Enter the cage number, mouse number, and date of birth in the respective fields.
4. Click the "Submit" button to add the data to the database.
5. To view the entire database, click the "Export" button. The data will be printed in the console as a Pandas DataFrame.
6. To delete data, enter either the cage number or mouse number in the respective field and click the "Delete Data" button. A confirmation dialog will appear before deleting the data.
7. After deleting data or before importing data, it clear the input fields.

## Code Structure

The application consists of two main classes:

1. `database.py`: Handles the database connections, queries, and operations.
2. `ui.py`: Builds the GUI using Tkinter and interacts with the `MouseDatabase` class.

The `main.py` file contains the main entry point for the application.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.