from sklearn.metrics import mean_squared_error

# Calculate MSE and RMSE
mse = mean_squared_error(y_test_scaled, predictions)
rmse = np.sqrt(mse)

print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
