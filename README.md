# 🚲 Project 1 — Bike Rental Demand Prediction (Regression)

A **Machine Learning regression project** that predicts bike rental demand based on weather conditions, time, and contextual factors. Includes a **Streamlit web app** for real-time predictions.

---

## 📋 Problem Statement

Bike-sharing systems need accurate demand forecasting to optimize fleet distribution. This project builds a regression model to predict hourly bike rental counts (`cnt`) using features like temperature, humidity, wind speed, season, and time of day.

---

## 📂 Project Files

| File | Description |
|------|-------------|
| `bike_rental.ipynb` | Complete EDA, feature engineering, model building & evaluation |
| `Dataset.csv` | Hourly bike rental dataset (17,379 records, 17 features) |
| `streamlit_app.py` | Streamlit deployment app for live predictions |
| `Business_Objective-P634.docx` | Business objective & problem statement document |
| `P634Bike Rental - Regression.pptx` | Project presentation |

---

## 📊 Dataset Features

| Feature | Description |
|---------|-------------|
| `season` | Season (Spring, Summer, Fall, Winter) |
| `yr` | Year (2011, 2012) |
| `mnth` | Month (1–12) |
| `hr` | Hour of day (0–23) |
| `holiday` | Whether the day is a holiday |
| `weekday` | Day of the week (0–6) |
| `workingday` | Whether it's a working day |
| `weathersit` | Weather condition (1=Clear, 2=Mist, 3=Light Snow/Rain, 4=Heavy Rain) |
| `temp` | Normalized temperature |
| `hum` | Normalized humidity |
| `windspeed` | Normalized wind speed |
| `cnt` | **Target** — Total bike rental count |

---

## 🚀 How to Deploy with Streamlit

### Step 1 — Clone the Repository

```bash
git clone https://github.com/APPISETTYHARI/Project-1-Bike-Rental-Regression.git
cd Project-1-Bike-Rental-Regression
```

### Step 2 — Install Dependencies

```bash
pip install streamlit joblib numpy scikit-learn
```

### Step 3 — Generate the Model (if `bike_model.pkl` doesn't exist)

Open and run the Jupyter notebook to train the model and save it:

```bash
jupyter notebook bike_rental.ipynb
```

> **Note:** Make sure the notebook saves the trained model as `bike_model.pkl` using:
> ```python
> import joblib
> joblib.dump(model, "bike_model.pkl")
> ```

### Step 4 — Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

This will open the app in your browser at `http://localhost:8501`

### Step 5 — Use the App

The app provides interactive sliders and dropdowns for:

| Input | Control |
|-------|---------|
| 🌡️ Temperature | Slider (0–50°C) |
| 💧 Humidity | Slider (0–100%) |
| 🌬️ Wind Speed | Slider (0–50) |
| 🌦️ Weather Condition | Dropdown (1–4) |
| 🍂 Season | Dropdown (1–4) |
| 📅 Month | Slider (1–12) |
| 📆 Day of Week | Slider (0=Sun – 6=Sat) |
| 🕐 Hour of Day | Slider (0–23) |
| 🎉 Holiday | Yes / No |
| 💼 Working Day | Yes / No |

Click **"Predict Demand"** to get the predicted bike rental count!

---

## 🛠️ Tech Stack

- **Python** — Core language
- **Pandas & NumPy** — Data manipulation
- **Matplotlib & Seaborn** — Visualization
- **Scikit-learn** — ML model training (Regression)
- **Joblib** — Model serialization
- **Streamlit** — Web app deployment

---

## 📄 License

This project is for educational purposes as part of a Data Science course.

---

<p align="center">Made with ❤️ by <strong><a href="https://linkedin.com/in/appisettyhari">APPISETTY HARI</a></strong></p>
