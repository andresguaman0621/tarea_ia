# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary Data.csv')

# Removing rows with NaN values
dataset = dataset.dropna()
print(f"Dataset shape after removing NaN values: {dataset.shape}")

X = dataset.iloc[:, 4:5].values  # Years of Experience
y = dataset.iloc[:, 5].values    # Salary

# Training the Linear Regression model on the whole dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Training the Polynomial Regression model on the whole dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualising the Linear Regression results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Experience vs Salary (Linear Regression)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Experience vs Salary (Polynomial Regression)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Experience vs Salary (Polynomial Regression - High Resolution)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression
experience_to_predict = 6.5
prediction_linear = lin_reg.predict([[experience_to_predict]])
print(f"\nPredicting salary for {experience_to_predict} years of experience:")
print(f"Linear Regression Prediction: ${prediction_linear[0]:.2f}")

# Predicting a new result with Polynomial Regression
prediction_poly = lin_reg_2.predict(poly_reg.fit_transform([[experience_to_predict]]))
print(f"Polynomial Regression Prediction: ${prediction_poly[0]:.2f}")

# Evaluating the models
from sklearn.metrics import r2_score, mean_squared_error

# Linear Regression Evaluation
y_pred_lin = lin_reg.predict(X)
r2_lin = r2_score(y, y_pred_lin)
rmse_lin = np.sqrt(mean_squared_error(y, y_pred_lin))

# Polynomial Regression Evaluation
y_pred_poly = lin_reg_2.predict(poly_reg.fit_transform(X))
r2_poly = r2_score(y, y_pred_poly)
rmse_poly = np.sqrt(mean_squared_error(y, y_pred_poly))

print("\nModel Evaluation:")
print(f"Linear Regression - R²: {r2_lin:.4f}, RMSE: {rmse_lin:.2f}")
print(f"Polynomial Regression - R²: {r2_poly:.4f}, RMSE: {rmse_poly:.2f}")

# Coeficientes y fórmula del modelo lineal
print("\nLinear Regression Model:")
print(f"Formula: Salary = {lin_reg.coef_[0]:.2f} * Experience + {lin_reg.intercept_:.2f}")

# Coeficientes del modelo polinómico
print("\nPolynomial Regression Model (degree 4):")
print("Coefficients:")
for i, coef in enumerate(lin_reg_2.coef_):
    print(f"Coefficient {i}: {coef:.2f}")