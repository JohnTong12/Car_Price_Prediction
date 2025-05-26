# Car Price Predictor

The Car Price Predictor is a machine learning application designed to estimate the price of a car based on its specifications, such as brand, year, fuel type, horsepower, and more. Built with Streamlit, this user-friendly web app allows you to input car details and instantly receive a predicted price, making it a valuable tool for car buyers, sellers, and enthusiasts alike.

## Try the App (🌐)

Experience the Car Price Predictor online at [Car Price Predictor](https://carpriceprediction-jfdzvtprbneccuxcvn89ft.streamlit.app/). No installation required—just enter your car's details and get an instant price estimate!

## Project Overview (📖)

The Car Price Predictor uses a pre-trained XGBoost regression model to predict car prices accurately. The model was trained on a comprehensive dataset of car specifications, including both numerical and categorical features. Key features of this project include:

- **User-Friendly Interface**: Easy-to-use Streamlit app with input validation.
- **Accurate Predictions**: High-performance model with strong evaluation metrics.
- **Instant Results**: Get predictions in seconds.
- **Customizable Inputs**: Supports a wide range of car features for detailed predictions.

## Getting Started (🚀)

To run the Car Price Predictor locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/johntong12/car_price_prediction.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd car_price_prediction
   ```

3. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

5. **Install Dependencies**:
   Ensure you have a `requirements.txt` file with the necessary packages:
   ```
   streamlit
   pandas
   scikit-learn
   xgboost
   pydantic
   numpy
   ```
   Install them using:
   ```bash
   pip install -r requirements.txt
   ```

6. **Prepare Files**:
   - Place `car_price_data_cleaned.csv` in the project root directory.
   - Place `xgb_pipeline.pkl` in the `models` subdirectory.

7. **Run the App**:
   ```bash
   streamlit run car_price_app.py
   ```

The app will open in your web browser, where you can input car details and get predictions.

## How to Use (🖥️)

Once the app is running, you'll see input fields for various car specifications:

- **Brand**: Select from a list of available car manufacturers.
- **Year**: Enter the model year (1990–2017).
- **Fuel Type**: Choose the type of fuel (e.g., gasoline, diesel).
- **Horsepower**: Enter the engine horsepower (0–1001).
- **Cylinders**: Select the number of cylinders (0–16).
- **Transmission**: Choose the transmission type (e.g., automatic, manual).
- **Drive Type**: Select the drive configuration (e.g., AWD, FWD).
- **Doors**: Choose the number of doors (2, 3, 4).
- **Vehicle Size**: Select the size category (e.g., compact, midsize).
- **Highway MPG**: Enter the highway fuel efficiency (7–128).
- **City MPG**: Enter the city fuel efficiency (8–137).
- **Popularity**: Enter the popularity index (2–5657).

After filling in the details, click "Predict" to see the estimated price. Use the "Reset All" button to clear the inputs and start over.

## Model Details (📊)

The Car Price Predictor uses an XGBoost regression model, selected for its high accuracy and efficiency. The model is part of a scikit-learn pipeline that includes:

- **Numerical Features Pipeline**:
  - Imputation (mean strategy)
  - Winsorization (1% quantiles to handle outliers)
  - Standardization

- **Categorical Features Pipeline**:
  - Imputation (most frequent strategy)
  - One-hot encoding

The target variable is the car's price, which was not transformed (e.g., no log transformation was applied in the final model).

### Performance Metrics

The model was evaluated on a test set with the following results:

- **Mean Absolute Error (MAE)**: 4,712.25
- **Mean Squared Error (MSE)**: 80,267,576.0
- **Root Mean Squared Error (RMSE)**: 8,959.22
- **R² Score**: 0.9578
- **Mean Absolute Percentage Error (MAPE)**: 0.1901

For more detailed information on the model training and evaluation, refer to the Jupyter Notebook in the repository.

## Project Structure (📂)

The project directory is organized as follows:

- `car_price_app.py`: The main Streamlit application script.
- `car_price_data_cleaned.csv`: The dataset used for training and unique value extraction.
- `models/xgb_pipeline.pkl`: The pre-trained XGBoost model pipeline.
- `requirements.txt`: List of Python dependencies required to run the app.
- `README.md`: This documentation file.

## Troubleshooting (🛠️)

If you encounter issues while setting up or running the app, here are some common solutions:

- **Missing Model File**: Ensure `xgb_pipeline.pkl` is in the `models` directory. If missing, retrain the model using the provided Jupyter Notebook.
- **Dependency Errors**: Check that all dependencies listed in `requirements.txt` are installed. Run `pip install -r requirements.txt` to ensure all packages are up to date.
- **Input Errors**: Make sure all input fields are filled correctly within the specified ranges. For example, Year must be between 1990 and 2017.

If you face other issues, feel free to open an issue on the GitHub repository or contact the maintainer.

## Contributing (🤝)

Contributions to this project are welcome! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear commit messages.
4. Push your branch and submit a pull request.

Please ensure your code follows PEP 8 guidelines and includes necessary documentation.

## License (📜)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments (🙌)

- **Dataset**: [Kaggle Car Price Prediction Dataset](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes) (please update if the dataset source differs).
- **Tools and Libraries**:
  - [Streamlit](https://streamlit.io/) for the web app framework.
  - [Scikit-learn](https://scikit-learn.org/) for machine learning pipelines.
  - [XGBoost](https://xgboost.readthedocs.io/) for the regression model.
  - [Pandas](https://pandas.pydata.org/) for data manipulation.
  - [Pydantic](https://pydantic-docs.helpmanual.io/) for input validation.

## Contact (📬)

For questions, feedback, or suggestions, please contact:

- GitHub: [johntong12](https://github.com/johntong12)
- Email: [your_email@example.com] (please replace with your actual email)

Happy predicting car prices! 🎉
