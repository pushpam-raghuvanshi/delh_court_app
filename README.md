
# 🏛️ Delhi High Court Case Data Fetcher & Mini Dashboard

This is a web application built using **Flask** and **Selenium** that allows users to search for live Delhi High Court case data by entering the Case Type, Number, and Year. The app scrapes official data from the Delhi High Court website and presents it in a clean, styled interface. It also allows downloading a PDF report of the case details.

---

## 🔍 Features

- Search for live **Delhi High Court** case status using:
  - Case Type (e.g., W.P. (C), FAO, etc.)
  - Case Number
  - Year
- View important case details:
  - Case Title, Petitioner, Respondent, Bench, Status
  - Last & Next Hearing Dates
- Download a PDF of the case details
- Clean and responsive UI (HTML + CSS)

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Scraping**: Selenium with ChromeDriver & WebDriverManager
- **Frontend**: HTML5, CSS3 (Jinja templates)
- **PDF Generation**: `xhtml2pdf`

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.7+
- Google Chrome browser (version ~138 or compatible)

### 🔧 Installation Steps

1. Clone or extract the project folder:

   ```
   Delhi_High_Court_App/
   ├── app.py
   ├── scraper.py
   ├── templates/
   ├── static/
   ├── requirements.txt
   └── README.md
   ```

2. Open a terminal inside the folder and create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask app:

   ```bash
   python app.py
   ```

6. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

---

## 📝 Usage

1. Select a case type (e.g., W.P. (C))
2. Enter the case number (e.g., 5173)
3. Enter the year (e.g., 2023)
4. Click on **Search**
5. View the case details and download the PDF if needed

---

## 📄 Sample Case to Try

- **Case Type**: W.P. (C)  
- **Case Number**: 5173  
- **Year**: 2023

---

## 📁 Folder Structure

```
Delhi_High_Court_App/
│
├── app.py                 # Main Flask application
├── scraper.py             # Selenium-based scraper
├── requirements.txt       # All dependencies
├── README.md              # Project documentation
│
├── templates/             # HTML Templates
│   ├── index.html
│   ├── result.html
│
├── static/                # Static CSS files
│   └── style.css
```

---

## 📃 PDF Report Feature

- After searching for a case, click **"Download PDF"** to generate a formatted PDF report of all key details.
- Uses `xhtml2pdf` under the hood.

---

## 👨‍💻 Author

- **Pushpam Raghuvanshi**
- Developed as part of an internship screening task.

---

## 📌 Notes

- This app uses **live web scraping**. If the Delhi High Court website structure changes, scraping may break.
- Tested on Chrome version `138.0.7204.183`.

---

## 🏁 Future Enhancements (Optional)

- Add support for other Indian courts (e.g., District Courts, Supreme Court)
- Add search history or login system
- Deploy on cloud (e.g., Render, Railway)

---

## 📞 Contact

If you are a recruiter reviewing this project and need help running it, please reach out to me on my contact email or LinkedIn (if submitted).
