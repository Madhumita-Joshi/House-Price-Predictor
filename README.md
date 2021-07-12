# House-Price-Predictor
This House Price Predictor is a Machine Learning Model written in Python that uses Linear Regression for analyzing current house prices and forecasting the future prices according to the user’s requirements.It takes  18 inputs such as No. of Bedrooms,No of Bathrooms,Sq ft Area etc and predicts the house price.The model has been trained using USA_Housing_dataset.A number of data cleaning methods are deployed before fitting the model.The model has been integrated with a flask frontend.
The following inputs are required:

1. date: Date the house was sold
2. price: Price is the prediction target
3. bedrooms: Number of Bedrooms/House
4. bathrooms: Number of bathrooms/bedrooms
5. sqft_living: Square footage of the home
6. sqft_lot: Square footage of the lot
7. floors: Total floors (levels) in the house
8. waterfront: House which has a view to a waterfront
9. view: Has been viewed
10.condition: How good the condition is Overall
11.sqft_above: Square footage of house apart from basement
12.sqft_basement: Square footage of the basement
13.yr_built: Year the house was built
14.yr_renovated: Year when house was renovated
15.street: Street name of the house
16.city: City in which the house isPage | 6
17.statezip: State zip code
18.country: Country in which the house is

The project helps you understand the correlation between the different attributes and the house price.It makes use of visualizations and plots making it easier to identify trends.The accuracy of this model is found by callculating RMSE (Root mean square error) and MAE(Mean Absolute Error)

How to run the project:
1) Install Python and pip on your system.
2) Install the pyton virtual environment by running py -v -m venv nameofdirectory in your command prompt.
3) Activate the virtual environment by the running command nameofdirectory\Scripts\activate
4) Install flask using pip install flask.
5) Download the House_price_predictor folder.
6) Navigate to the House_price_predictor folder in command prompt and run the command python app.py
7) Enter the address http://127.0.0.1:5000/ in the url bar of your browser to access the dashboard of the Hous_price_predictor.
