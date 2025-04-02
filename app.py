import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import load_model
model_path = 'stock_price_prediction.keras'  # Ensure this model exists in the directory
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()
st.title("📈 Stock Price Prediction")
stock = st.text_input('Enter the stock ticker', 'GOOG')

if stock:
    st.write(f"**Selected stock ticker:** {stock}")
    start_date = "2010-01-01"
    end_date = "2024-12-31"

    st.write("Fetching stock data... ⏳")
    data = yf.download(stock, start=start_date, end=end_date)

    if data.empty:
        st.error(f"No stock data found for {stock}. Please try another ticker.")
    else:
        st.success("Stock data retrieved successfully! ✅")
        st.subheader("Data from 2010-2024")
        st.write(data)
        data_train = data[['Close']].iloc[:int(len(data) * 0.80)]
        data_test = data[['Close']].iloc[int(len(data) * 0.80):]
        scaler = MinMaxScaler(feature_range=(0,1))
        past_100_days = data_train.tail(100)
        data_test = pd.concat([past_100_days, data_test], ignore_index=True)
        scaled_data_train = scaler.fit_transform(data_test)

        st.subheader("Price vs Moving Averages")
        ma_50_days = data['Close'].rolling(50).mean()
        ma_100_days = data['Close'].rolling(100).mean()

        fig1 = plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], 'g', label='Actual Price')
        plt.plot(ma_50_days, 'r', label='50-day MA')
        plt.plot(ma_100_days, 'b', label='100-day MA')
        plt.legend()
        plt.title("Stock Price with MA50 & MA100")
        st.pyplot(fig1)

        x_train, y_train = [], []
        for i in range(100, scaled_data_train.shape[0]):
            x_train.append(scaled_data_train[i-100:i])
            y_train.append(scaled_data_train[i, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)

        predicted_price = model.predict(x_train)
        scale_factor = 1 / scaler.scale_
        y_predicted = predicted_price * scale_factor
        y_test = y_train * scale_factor

        mae = mean_absolute_error(y_test, y_predicted)
        mse = mean_squared_error(y_test, y_predicted)

        st.subheader("📊 Model Accuracy")
        st.write(f"🔹 **Mean Absolute Error (MAE):** {mae:.2f}")
        st.write(f"🔹 **Mean Squared Error (MSE):** {mse:.2f}")

        st.subheader("📉 Original Price vs Predicted Price")
        fig2 = plt.figure(figsize=(10, 5))
        plt.plot(y_test, 'g', label='Actual Price')
        plt.plot(y_predicted, 'r', linestyle='dashed', label='Predicted Price')
        plt.legend()
        plt.title("Stock Price Prediction")
        st.pyplot(fig2)

st.write("🔹 Enter a valid stock ticker to see predictions.")
