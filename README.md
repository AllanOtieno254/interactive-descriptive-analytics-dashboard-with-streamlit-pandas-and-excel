# 📊 Descriptive Data Analytics Dashboard using Streamlit, Pandas, Plotly & Excel

Welcome to this powerful, interactive, and visually rich **Descriptive Analytics Dashboard** built using **Streamlit**, **Pandas**, **Plotly**, and **Excel**. This project demonstrates the capabilities of building a modern business intelligence dashboard with dynamic filters, KPIs, trend graphs, and a visually engaging interface—all from a simple Excel file.

---

## 🧠 Project Objective

The goal of this project is to provide a **user-friendly interface** for exploring investment data using modern visualization tools. It allows business users and analysts to:

- Understand key business metrics.
- Visualize investment trends.
- Filter data dynamically.
- Track performance against targets.

---

## 🛠️ Tools & Technologies Used

| Tool              | Purpose                              |
|------------------|--------------------------------------|
| Streamlit        | Building interactive web dashboards  |
| Pandas           | Data manipulation and filtering      |
| Plotly           | Interactive visualizations (bar, pie, line charts) |
| Openpyxl         | Reading Excel files in Python        |
| Numerize         | Human-readable numeric formatting    |
| Streamlit Option Menu | Sidebar navigation styling      |
| CSS              | UI Styling for Streamlit             |

---

## ✨ Features

✅ Side navigation with icons  
✅ KPI cards with metrics (Sum, Mean, Median, Mode, Rating)  
✅ Pie, bar, and line charts with Plotly  
✅ Progress bar with animation and target tracking  
✅ Live data filtering by Region, Location, and Construction  
✅ Responsive layout using Streamlit's `columns()`  
✅ Embedded custom CSS for polished UI  
✅ Lightweight and easy to deploy (no database needed)  

---

## 🧠 Concepts Demonstrated
Feature-based filtering

Descriptive statistics (Sum, Mean, Median, Mode)

Custom CSS in Streamlit

Sidebar navigation using streamlit-option-menu

Multi-chart layouts with responsive design

Real-time progress bar animation

Clean dashboard design with accessibility in mind

## 🧱 Project Structure

```plaintext
descriptive-data-analytics-dashboard/
├── assets/
│   └── logo.png                  # Optional: your brand or logo
├── data/
│   └── data.xlsx                 # Excel dataset used in the dashboard
├── scripts/
│   └── dashboard_app.py          # Main Streamlit app file
├── screenshots/
│   └── dashboard_preview.png     # UI preview images (for README)
├── .gitignore                    # Ignore virtual environments, pycache, etc.
├── LICENSE                       # MIT License file
├── README.md                     # You're reading it 🙂
└── requirements.txt              # All required Python packages
