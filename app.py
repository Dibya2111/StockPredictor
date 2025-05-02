import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import load_model
import time

st.set_page_config(layout="wide")

# 📌 Safe data download with retries and caching
@st.cache_data(ttl=3600)
def safe_download(ticker, start, end, retries=5, delay=5):
    for attempt in range(retries):
        try:
            data = yf.download(ticker, start=start, end=end, progress=False, threads=False)
            if not data.empty:
                return data
            else:
                st.warning(f"No data received. Retry {attempt+1}/{retries}...")
        except Exception as e:
            st.warning(f"Download error: {e}. Retry {attempt+1}/{retries}...")
        time.sleep(delay)
    return pd.DataFrame()

# 📌 Load model
model_path = 'stock_price_prediction.keras'
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

    with st.spinner("Fetching stock data... ⏳"):
        data = safe_download(stock, start=start_date, end=end_date)

    if data.empty:
        st.error("❌ Too many requests or invalid ticker. Please try again later.")
        st.stop()

    st.success("Stock data retrieved successfully! ✅")
    st.subheader("Data from 2010–2024")
    st.dataframe(data.tail())

    # Prepare data
    data_close = data[['Close']]
    data_train = data_close.iloc[:int(len(data_close) * 0.80)]
    data_test = data_close.iloc[int(len(data_close) * 0.80):]

    full_data = pd.concat([data_train, data_test], ignore_index=True)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(full_data)

    # Prepare test input
    x_test, y_test = [], []
    test_start = len(data_train) - 100

    for i in range(100, len(scaled_data[test_start:])):
        x_test.append(scaled_data[test_start + i - 100:test_start + i])
        y_test.append(scaled_data[test_start + i, 0])

    x_test = np.array(x_test)
    y_test = np.array(y_test)

    st.write("✅ Test data shape:", x_test.shape)

    # Predict
    predicted_price = model.predict(x_test)
    scale_factor = 1 / scaler.scale_[0]
    y_predicted = predicted_price * scale_factor
    y_test_actual = y_test * scale_factor

    # Metrics
    mae = mean_absolute_error(y_test_actual, y_predicted)
    mse = mean_squared_error(y_test_actual, y_predicted)

    st.subheader("📊 Model Accuracy")
    st.write(f"🔹 **Mean Absolute Error (MAE):** {mae:.2f}")
    st.write(f"🔹 **Mean Squared Error (MSE):** {mse:.2f}")

    # Plot prediction
    st.subheader("📉 Original Price vs Predicted Price")
    fig2 = plt.figure(figsize=(10, 5))
    plt.plot(y_test_actual, 'g', label='Actual Price')
    plt.plot(y_predicted, 'r--', label='Predicted Price')
    plt.legend()
    plt.title("Stock Price Prediction")
    st.pyplot(fig2)

    # Moving Averages
    st.subheader("Price vs Moving Averages")
    ma_50 = data['Close'].rolling(50).mean()
    ma_100 = data['Close'].rolling(100).mean()

    fig1 = plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], 'g', label='Actual Price')
    plt.plot(ma_50, 'r', label='50-day MA')
    plt.plot(ma_100, 'b', label='100-day MA')
    plt.legend()
    plt.title("Stock Price with MA50 & MA100")
    st.pyplot(fig1)

st.write("🔹 Enter a valid stock ticker to see predictions.")
