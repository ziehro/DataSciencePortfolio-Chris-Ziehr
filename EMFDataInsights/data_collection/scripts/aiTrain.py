import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

# Step 1: Load the Data
data = pd.read_csv('scripts/emf_readings.csv')

# Step 2: Preprocess the Data
# For this example, let's assume the last column is the label
X = data.iloc[:, :-1]  # Features (excluding the label)
y = data.iloc[:, -1]   # Labels

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 4: Train the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the Model
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

