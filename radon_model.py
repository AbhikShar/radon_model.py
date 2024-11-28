import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Fake dataset
data = {
    "house_size": [1200, 1600, 2500, 1400, 1800, 2800, 2200, 1700, 2600, 3000,
                   1500, 2000, 3100, 1400, 2400, 1250, 2300, 2700, 1300, 1950],
    "radon_level": [95, 45, 230, 110, 65, 320, 150, 85, 210, 190, 55, 130, 275,
                    100, 180, 75, 200, 290, 50, 170]
}

# Convert data to numpy arrays
X = np.array(data["house_size"]).reshape(-1, 1)
y = np.array(data["radon_level"])

# Split into training and testing sets (80-20 split)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title('Relationship Between House Size and Radon Levels')
plt.xlabel('House Size (sq ft)')
plt.ylabel('Radon Level (Bq/m³)')
plt.legend()
plt.show()
