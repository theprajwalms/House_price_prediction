
# 🏠 Linear Regression on USA Housing Data

## 📌 Project Overview
This project demonstrates how to build a **Linear Regression model** to predict housing prices based on real-world housing data. It covers data exploration, visualization, model building, evaluation, and interpretation of results.

## 📊 Dataset
- **Name**: USA_Housing.csv
- **Features**:
  - Avg. Area Income
  - Avg. Area House Age
  - Avg. Area Number of Rooms
  - Avg. Area Number of Bedrooms
  - Area Population
  - Price (Target)

## 🛠️ Tools & Libraries Used
- Python
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn

## 🔍 Workflow
1. Data Loading and Inspection
2. Exploratory Data Analysis (EDA)
3. Data Visualization
4. Linear Regression Model Training
5. Model Evaluation (MAE, MSE, RMSE)
6. Residuals Analysis
7. Interpretation of Coefficients
8. Summary Conclusion

## 📈 Model Performance
- The model shows good predictive accuracy using metrics like:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
- Residuals are normally distributed, indicating a good model fit.

## 📌 Key Takeaways
- Avg. Area Income and Number of Rooms are the most influential features.
- Linear Regression is an effective baseline model for price prediction in structured datasets.

## 📁 How to Run
1. Clone the repository
2. Install required packages using:
   ```
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook:
   ```
   01-Linear Regression with Python.ipynb
   ```

## 🏡 Predicting a New House Price
To demonstrate the application of the trained Linear Regression model, we input custom values for a hypothetical house:

- Avg. Area Income = 60,000  
- Avg. Area House Age = 5  
- Avg. Area Number of Rooms = 7  
- Avg. Area Number of Bedrooms = 4  
- Area Population = 30,000

💡 Example prediction: For these input values, the model predicted a house price of **$795,981.70**.

## 🚀 Streamlit App

An interactive app was built using **Streamlit** to showcase the trained linear regression model.

### ▶️ How to Run the App Locally:
1. Install Streamlit (if not already):
   ```
   pip install streamlit
   ```

2. From the terminal, run:
   ```
   streamlit run app.py
   ```

The app allows users to input features like:
- Average Area Income
- House Age
- Number of Rooms and Bedrooms
- Area Population

And it returns the **predicted house price** in real-time.

This adds practical, real-world usability to the model.

## 👨‍🎓 Author
**Prajwal M.S**  
Recent Data Science Graduate | Python & ML Enthusiast
