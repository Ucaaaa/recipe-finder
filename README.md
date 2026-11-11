# Recipe Finder

A simple web application built with **Python**, **Flask**, and **TheMealDB API** to search for food recipes and view their details.

## Features

- Search recipes by meal or food name.
- Display recipe cards with meal images, category, and origin.
- Open a recipe detail page.
- View ingredients, measurements, and cooking instructions.
- Retrieve recipe data from the public [TheMealDB API](https://www.themealdb.com/api.php).

## Tech Stack

- Python
- Flask
- Requests
- HTML5 and CSS3
- TheMealDB API

## Project Structure

```text
recipe-finder/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── detail.html
└── screenshots/
    └── README.md
```

## Requirements

- Python 3.9 or newer
- Internet connection (the application requests data from TheMealDB API)

## Installation and Run

### 1. Clone the repository

```bash
git clone https://github.com/ YOUR-USERNAME /recipe-finder.git
cd recipe-finder
```

Replace `YOUR-USERNAME` with your GitHub username. Remove the spaces around the slash in the clone URL.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open the local address shown in the terminal (by default, `http://127.0.0.1:5000`).

Press `Ctrl + C` in the terminal to stop the server.

## Screenshots

Add screenshots of the running application to the `screenshots/` directory. See `screenshots/README.md` for suggested filenames.

## API and Attribution

Recipe information and images are provided by [TheMealDB](https://www.themealdb.com/). The application requires an internet connection to search for recipes and load recipe details.

## Notes

- The virtual environment (`.venv/`), Python cache files, and local editor settings are intentionally excluded from Git.
- This project is intended for learning and demonstration purposes.
