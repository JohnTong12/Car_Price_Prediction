import streamlit as st
import pandas as pd
import pickle as pkl
from pydantic import BaseModel, Field
import os

# Load the pre-trained pipeline
pipeline_path = os.path.join(os.path.dirname(__file__), "models", "xgb_pipeline.pkl")
with open(pipeline_path, "rb") as file:
    pipeline = pkl.load(file)

# Load the dataset to get unique values
@st.cache_data
def load_data():
    data_path = os.path.join(os.path.dirname(__file__), "car_price_data_cleaned.csv")
    return pd.read_csv(data_path)

data = load_data()

# Get unique values for categorical columns
brands = sorted(data['Brand'].unique())
fuel_types = sorted(data['Fuel_Type'].dropna().unique())
transmissions = sorted(data['Transmission'].unique())
drive_types = sorted(data['Drive_Type'].unique())
vehicle_sizes = sorted(data['Vehicle_Size'].unique())
doors_options = sorted(data['Doors'].unique())
cylinders_options = sorted(data['Cylinders'].unique())

# Pydantic model for input validation
class CarInput(BaseModel):
    Brand: str
    Year: int = Field(..., ge=1990, le=2017)
    Fuel_Type: str
    Horsepower: float = Field(..., ge=0.0, le=1001.0)
    Cylinders: float = Field(..., ge=0.0, le=16.0)
    Transmission: str
    Drive_Type: str
    Doors: float = Field(..., ge=2.0, le=4.0)
    Vehicle_Size: str
    Highway_MPG: int = Field(..., ge=7, le=128)
    city_mpg: int = Field(..., ge=8, le=137)
    Popularity: int = Field(..., ge=2, le=5657)

# Prediction function
def predict(car_data: CarInput):
    input_data = pd.DataFrame([car_data.dict()])
    prediction = pipeline.predict(input_data)[0]
    return prediction

def main():
    # Streamlit UI
    bg = """<div style='background-color:black; padding:13px'>
            <h1 style='color:white'>🚘 CAR PRICE PREDICTOR</h1>
            </div>"""
    st.markdown(bg, unsafe_allow_html=True)

    # Initialize session state for widget keys
    if "reset_trigger" not in st.session_state:
        st.session_state.reset_trigger = 0

    # Car Specifications
    st.subheader("Car Specifications")
    left, right = st.columns(2)

    with left:
        Brand = st.selectbox("Brand", brands, help="Select the car manufacturer", key=f"brand_{st.session_state.reset_trigger}")
        Year = st.number_input("Year", min_value=1990, max_value=2017, value=2010, step=1, help="Enter the model year", key=f"year_{st.session_state.reset_trigger}")
        Fuel_Type = st.selectbox("Fuel Type", fuel_types, help="Select the type of fuel", key=f"fuel_type_{st.session_state.reset_trigger}")
        Transmission = st.selectbox("Transmission", transmissions, help="Select the transmission type", key=f"transmission_{st.session_state.reset_trigger}")
        Drive_Type = st.selectbox("Drive Type", drive_types, help="Select the drive configuration", key=f"drive_type_{st.session_state.reset_trigger}")
        Vehicle_Size = st.selectbox("Vehicle Size", vehicle_sizes, help="Select the vehicle size category", key=f"vehicle_size_{st.session_state.reset_trigger}")

    with right:
        Horsepower = st.number_input("Horsepower", min_value=0.0, max_value=1001.0, value=200.0, step=1.0, help="Enter the engine horsepower", key=f"horsepower_{st.session_state.reset_trigger}")
        Cylinders = st.selectbox("Cylinders", cylinders_options, help="Select the number of cylinders", key=f"cylinders_{st.session_state.reset_trigger}")
        Doors = st.selectbox("Doors", doors_options, help="Select the number of doors", key=f"doors_{st.session_state.reset_trigger}")
        Highway_MPG = st.number_input("Highway MPG", min_value=7, max_value=128, value=25, step=1, help="Enter highway fuel efficiency", key=f"highway_mpg_{st.session_state.reset_trigger}")
        city_mpg = st.number_input("City MPG", min_value=8, max_value=137, value=20, step=1, help="Enter city fuel efficiency", key=f"city_mpg_{st.session_state.reset_trigger}")
        Popularity = st.number_input("Popularity", min_value=2, max_value=5657, value=1000, step=1, help="Popularity index of the car", key=f"popularity_{st.session_state.reset_trigger}")

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        predict_button = st.button("Predict")
    with col2:
        reset_button = st.button("Reset All")

    # Handle Reset All
    if reset_button:
        st.session_state.reset_trigger += 1
        st.success("All fields reset successfully!", icon="🔄")

    # Handle Predict
    if predict_button:
        try:
            car_data = CarInput(
                Brand=Brand,
                Year=Year,
                Fuel_Type=Fuel_Type,
                Horsepower=Horsepower,
                Cylinders=Cylinders,
                Transmission=Transmission,
                Drive_Type=Drive_Type,
                Doors=Doors,
                Vehicle_Size=Vehicle_Size,
                Highway_MPG=Highway_MPG,
                city_mpg=city_mpg,
                Popularity=Popularity
            )
            prediction = predict(car_data)
            st.markdown(
                f"<div style='background-color:#d4edda; padding:10px; border-radius:5px;'>"
                f"<h3 style='color:#155724;'>✅ Predicted Price: ${prediction:,.2f}</h3>"
                "</div>",
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()