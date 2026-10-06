Title of ML Project:  Food order delivery time  Prediction Model
—-----------------------------------------------------------------------------------------------------------
Name: SAIDH FABIS M

Organization: Entri Elevate

Date:06-10-202

—--------------------------------------------------------------------------------------------------------

1.	Overview of Problem Statement:


The Food Order Delivery Dataset contains information about food orders, delivery distance, traffic conditions, driver availability, vehicle type, and delivery duration. The objective of this project is to build a machine learning regression model to predict Delivery_Duration_Minutes. The model will analyze different factors affecting delivery time and provide accurate delivery-time predictions. This can help food delivery businesses improve delivery planning, operational efficiency, and customer satisfaction.

2. Objective:
To develop a machine learning regression model that accurately predicts food delivery duration based on various order and delivery-related factors.

3. Data Description:

   - Source: Kaggle , link: Food Order Delivery Dataset
   - Features: 
     Order_ID, User_ID, Restaurant_ID, Driver_ID, Item_Name, Quantity, Total_Price, 
     Order_Time, Delivery_Time, City, Payment_Method, Order_Status, 
     Driver_Vehicle,Restaurant_Lat, Restaurant_Lon, Customer_Lat, Customer_Lon, 
     Driver_Lat,     Driver_Lon, Delivery_Distance_km, Traffic_Level, and
     Driver_Availability.

     Target: Delivery_Duration_Minutes



# Project Steps

The project includes the following steps:

- Data loading
- Data exploration
- Data cleaning
- Missing value checking
- Duplicate checking
- Outlier detection
- Skewness analysis
- Exploratory Data Analysis (EDA)
- Feature engineering
- Categorical data encoding
- Feature scaling
- Feature selection
- Train-test split
- Model building
- Model evaluation
- Hyperparameter tuning
- Pipeline creation
- Model saving
- Prediction using unseen data

---

## Machine Learning Models Used

The following regression algorithms were implemented:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor
4. AdaBoost Regressor
5. Support Vector Regressor (SVR)
6. MLP Regressor

---

## Model Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The model with the highest R² score and lower error values was considered the best-performing model.

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## Target Variable

`Delivery_Duration_Minutes`

---

## Important Features

Some of the features used for prediction include:

- Quantity
- Total Price
- City
- Payment Method
- Driver Vehicle
- Delivery Distance
- Traffic Level
- Driver Availability
- Order Hour
- Order Day of Week

---

## Conclusion

This project demonstrates how machine learning regression models can be used to predict food delivery duration.

The model can help food delivery businesses improve delivery-time estimation, operational planning, and customer satisfaction.

---

## Future Improvements

Future improvements may include:

- Adding weather information
- Using real-time traffic data
- Including restaurant preparation time
- Adding driver experience information
- Testing advanced models such as XGBoost and LightGBM
- Periodically retraining the model with new data

---

## Author

SAIDH FABIS M
