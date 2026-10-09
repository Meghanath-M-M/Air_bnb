# 🏠 Airbnb NYC Nightly Price Predictor

A Machine Learning regression system that predicts the estimated nightly rental price of an Airbnb property in New York City based on property, location, review, and availability information.

The project includes complete data analysis, feature engineering, model comparison, evaluation, explainability, and a Streamlit web application for making predictions.

---

## 📌 Project Overview

The goal of this project is to develop an end-to-end Machine Learning regression system capable of predicting the nightly rental price of Airbnb properties in New York City.

The system takes information such as:

- Neighbourhood
- Neighbourhood group
- Latitude and longitude
- Room type
- Minimum nights
- Number of reviews
- Reviews per month
- Host listing count
- Availability throughout the year

and predicts the estimated nightly Airbnb price.

---

## 🎯 Problem Statement

> Develop an end-to-end Machine Learning regression system that predicts the nightly rental price of an Airbnb property in New York City.

This is a **regression problem** because the target variable, `price`, is a continuous numerical value.

---

## 📊 Dataset

The project uses an Airbnb NYC dataset containing **30,000 records and 16 columns**.

### Important Features

| Feature | Description |
|---|---|
| `neighbourhood_group` | Major NYC area such as Manhattan or Brooklyn |
| `neighbourhood` | Specific neighbourhood |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |
| `room_type` | Type of Airbnb accommodation |
| `minimum_nights` | Minimum number of nights required |
| `number_of_reviews` | Total number of reviews |
| `reviews_per_month` | Average monthly reviews |
| `calculated_host_listings_count` | Number of listings managed by the host |
| `availability_365` | Number of days available in a year |
| `price` | Target variable — nightly rental price |

---

## 🔄 Machine Learning Workflow

The project follows an end-to-end Machine Learning workflow:

```text
Dataset
   ↓
Data Loading
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Comparison
   ↓
Model Evaluation
   ↓
Model Explainability
   ↓
Model Serialization
   ↓
Streamlit Deployment
