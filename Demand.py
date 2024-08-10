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
    temp['year'] = date.year
    temp['month'] = date.month
    temp['day'] = date.day
    temp['day_of_week'] = date.weekday() + 1  # Assuming Monday is 1
    temp['is_weekend'] = int(date.weekday() >= 5)  # 5 for Saturday and 6 for Sunday
    future_data = pd.concat([future_data, temp], ignore_index=True)

# Predicting Quantity using the model 'rf' defined and trained in the same notebook
future_data['Predicted_Quantity'] = rf.predict(future_data[['outlet_id', 'Sub_cat_id', 'Item_code', 'Price', 'year', 'month', 'day', 'day_of_week', 'is_weekend']])

# Group by to aggregate predicted quantities by outlet_id, Sub_cat_id, and Item_code
monthly_demand = future_data.groupby(['outlet_id', 'Sub_cat_id', 'Item_code']).agg({
    'Predicted_Quantity': 'sum'
}).reset_index()

# Output the results
print(monthly_demand)
