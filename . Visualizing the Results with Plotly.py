import plotly.graph_objs as go

# Create a plotly figure
fig = go.Figure()

# Add trace for actual prices
fig.add_trace(go.Scatter(x=stock_data.index[-len(y_test):], y=y_test_scaled.flatten(), mode='lines', name='Actual Price'))

# Add trace for predicted prices
fig.add_trace(go.Scatter(x=stock_data.index[-len(y_test):], y=predictions.flatten(), mode='lines', name='Predicted Price'))

# Add titles and labels
fig.update_layout(title='Tesla Stock Price Prediction', xaxis_title='Date', yaxis_title='Stock Price (USD)')

# Show the figure
fig.show()
