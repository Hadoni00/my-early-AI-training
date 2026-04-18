import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
# ===== device =====
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using:", device)
# ===== data =====
def create_data(n_samples=1000):
    X = torch.rand(n_samples, 4) * 10 
    y = (X[:, 0] * 2 + X[:, 1] * 1.5 + X[:, 2] * 3 + X[:, 3] * 5 + 5)
    return X, y.view(-1, 1)
X_train, y_train = create_data(2000)
# >>>gpu
X_train = X_train.to(device)
y_train = y_train.to(device)
class main(nn.Module):
    def __init__(self):
        super(main, self).__init__()
        self.hidden1 = nn.Linear(4, 24)
        self.hidden2 = nn.Linear(24, 8)
        self.output = nn.Linear(8, 1)
        self.relu = nn.ReLU() 
    def forward(self, x):
        x = self.relu(self.hidden1(x))
        x = self.relu(self.hidden2(x))
        x = self.output(x)
        return x
model = main().to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
# ===== train =====
epochs = 5000
for epoch in range(epochs):
    pred = model(X_train)
    loss = criterion(pred, y_train)
    optimizer.zero_grad() 
    loss.backward()      
    optimizer.step()     
    if (epoch + 1) % 50 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# ===== test =====
model.eval()
with torch.no_grad():
    test_input = torch.tensor([[5.0, 3.0, 4.0, 2.0]]).to(device)
    predicted_time = model(test_input)
    print(f'\nDự đoán: {predicted_time.item():.2f} phút')