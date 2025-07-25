# Predict stock prices on the test data
predictions = model.predict(x_test)

# Inverse transform the predictions back to original price scale
predictions = scaler.inverse_transform(predictions)

# Inverse transform the actual test data
y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))
