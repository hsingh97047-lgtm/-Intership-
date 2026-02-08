#Develop a linear regression model to predict house price based on features such as the number of rooms, location, size and other relevant factors. Collect a suitable dataset from Kaggle, preprocess it, and train the model to make accurate predictions.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("House Price Prediction Dataset.csv")

# Remove column spaces
df.columns = df.columns.str.strip()

print("Columns in dataset:", df.columns)

# Check target column
if "Price" not in df.columns:
    raise Exception("Price column not found. Check dataset column names.")

# Drop rows with missing target
df = df.dropna(subset=["Price"])

# Fill numeric missing values
num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical missing values
cat_cols = df.select_dtypes(include=['object', 'string']).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

# Encode categorical columns
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

# Features and target
X = df.drop("Price", axis=1)
y = df["Price"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest Model (Better than Linear Regression)
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)
print("Model Score:", model.score(X_test, y_test))
