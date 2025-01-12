
# Web Application for Displaying Data

This is a Python application that uses the Flask library to create a local web server, allowing us to test the tool using the web browser.

## Features

This application allows you to:
- Upload a `.csv` file
- Display the content of the `.csv` file in a table
- Select columns from the table
- Create different types of charts from the selected columns:
  - Scatter Plot
  - Line Plot
  - Bar Plot
  - Histogram

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000/` to start using the application.

## Usage

- Upload a `.csv` file via the web interface.
- The data from the `.csv` will be displayed as a table.
- You can select columns from the table to create charts.
- Choose one of the following chart types:
  - **Scatter plot**: Displays data points as individual dots.
  - **Line plot**: Displays data points connected by a line.
  - **Bar plot**: Displays data as bars.
  - **Histogram**: Displays the distribution of values in a set of data.