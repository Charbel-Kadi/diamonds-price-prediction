# 💎 Diamond Price Prediction

A machine learning web application that predicts diamond prices based on their characteristics.

## 🚀 Project Overview
This project uses a **Random Forest Regressor** model trained on the Kaggle diamonds dataset to predict diamond prices. It features a REST API built with FastAPI and an interactive UI built with Streamlit.

## 🛠️ Tech Stack
- **Machine Learning:** Scikit-learn, Random Forest Regressor
- **Backend API:** FastAPI
- **Frontend UI:** Streamlit
- **Data Processing:** Pandas, NumPy

## 📁 Project Structure
```
diamonds-api/
├── main.py          → FastAPI backend
├── app.py           → Streamlit frontend
├── requirements.txt → Project dependencies
└── .gitignore       → Ignored files
```

## ⚙️ How to Run

**1. Install dependencies:**
```
pip install -r requirements.txt
```

**2. Start the API:**
```
uvicorn main:app --reload
```

**3. Start the UI:**
```
streamlit run app.py
```

## 📊 Features
- Carat, Cut, Color, Clarity
- Depth, Table, Length, Width, Height

## 🎯 Output
Predicted diamond price in USD 💰
