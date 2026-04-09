import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

# Train model once
data = pd.read_csv('reflection_coefficient_dataset.csv')

X = data[['ZL', 'Z0']]
y = data['Gamma']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = MLPRegressor(hidden_layer_sizes=(20,10), max_iter=3000)
model.fit(X_scaled, y)

def predict_gamma(ZL, Z0):
    input_data = scaler.transform([[ZL, Z0]])
    pred = model.predict(input_data)[0]

    actual = (ZL - Z0) / (ZL + Z0)

    return pred, actual