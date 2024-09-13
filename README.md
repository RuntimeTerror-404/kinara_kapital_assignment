# Student Grid System with Server-side Filtering

This project is a coding assignment to develop a grid system that displays student details with pagination and server-side filtering. The project uses a **Flask** backend and a **React** frontend.

## Prerequisites

Please make sure that the following tools are installed on your local machine:
- **Python** (version 3.x)
- **Node.js** (version 14.x or higher)
- **npm** (comes with Node.js)

---

# There are two folders: Backend and Frontend, Backend stores the app.py main file and add_data_to_DB.py

## Backend Setup (Flask API) - Backend Folder

1. For Backend setup virtual environment will be preffered to aovid conflicts
- Modules/packages to  be installed:  **Flask**, **SQLite**, **Flask-CORS**
- Steps to run Flask app and test apis:
    # Delete instance folder (this folder will be created again when we run app.py).
    # Run app.py using command "python app.py" (for windows) -> it will create instance folder with     students.db inside it.
    # Run add_data_to_DB.py file to feed some sample data entries into the students.DB

- For testing Postman could be used (I use Thunder Client VS Code extension for api testing)


## Frontend Setup (React App) - Frontend Folder
- Run npm install and npm install axios 
- Needed code will be found in *StudentData.jsx* file where i'm fetching api data and make it visible here.


## Sequence: Delete instance folder -> run app.py -> run add_data_to_DB.py -> test api response -> run npm install and npm install axios in Frontend folder -> active server will send the data in ui.

-> Sample API endpoints:
- Get students with pagination: http://127.0.0.1:5000/students?page=1&page_size=10
- Get students with filtering:
- http://127.0.0.1:5000/students?page=1&page_size=10&name=John&total_marks=90


