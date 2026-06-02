# Traffic E-Challan Prediction System

## SDG Goal 16: Peace, Justice and Strong Institutions
This project predicts pending traffic challans using Machine Learning techniques.

## Problem Statement
Traffic departments often face large backlogs of pending challans. Predicting future pending challans helps authorities plan resources and improve efficiency.

## Dataset
Source: Delhi Traffic E-Challan Data
Rows: 4061

## Algorithms Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## Results
| Model | R² Score |
|---------|---------|
| Linear Regression | 0.980 |
| Decision Tree | 0.992 |
| Random Forest | 0.995 |
Random Forest achieved the best performance.

## Features Used
- disposedAmount
- pendingAmount
- pendingCourt
- disposedCourt
- totalCourt
- month
- day_of_week
- is_weekend

## Technologies
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib

## Future Scope
- Real-time challan prediction
- State-wise dashboard
- Traffic violation trend analysis
