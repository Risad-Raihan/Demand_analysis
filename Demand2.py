import pandas as pd

# Assuming 'df' is your DataFrame with historical data
# Creating the base structure for September 2024 with necessary feature columns
dates = pd.date_range('2024-09-01', '2024-09-30')
future_data = pd.DataFrame()

# Use unique combinations of outlet_id, Sub_cat_id, Item_code, and average Price from historical data
combinations = df[['outlet_id', 'Sub_cat_id', 'Item_code', 'Price']].drop_duplicates()

# Expand this combination across all days in September 2024
for date in dates:
    temp = combinations.copy()
    temp['date'] = date  # Store the full date for daily tracking
    temp['year'] = date.year
    temp['month'] = date.month
    temp['day'] = date.day
    temp['day_of_week'] = date.weekday() + 1  # Assuming Monday is 1
    temp['is_weekend'] = int(date.weekday() == 4)  # Set to 1 only if it's Friday
    future_data = pd.concat([future_data, temp], ignore_index=True)

# Predicting Quantity using the model 'rf' defined and trained in the same notebook
future_data['Predicted_Quantity'] = rf.predict(future_data[['outlet_id', 'Sub_cat_id', 'Item_code', 'Price', 'year', 'month', 'day', 'day_of_week', 'is_weekend']])

# The resulting DataFrame 'future_data' now includes a 'Predicted_Quantity' for each day
# You can output this DataFrame directly to see daily demand
print(future_data[['date', 'outlet_id', 'Sub_cat_id', 'Item_code', 'Predicted_Quantity']])
