import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
# Đầu vào (4 features): [Quãng đường(km), Đèn đỏ(cái), Tắc đường(1-5), Thời tiết(1-3)]
def create_data(n_samples=1000):
    X = torch.rand(n_samples, 4) * 10 
    # Công thức giả định: Time = dist*2 + red_lights*1.5 + traffic*3 + weather*5 + noise
    y = (X[:, 0] * 2 + X[:, 1] * 1.5 + X[:, 2] * 3 + X[:, 3] * 5 + 5)
    return X, y.view(-1, 1)
X_train, y_train = create_data(1000)
class main(nn.Module):
    def __init__(self):
        super(main, self).__init__()
        self.hidden1 = nn.Linear(4, 16)
        self.hidden2 = nn.Linear(16, 8)
        self.output = nn.Linear(8, 1)
        self.relu = nn.ReLU() 

    def forward(self, x):
        x = self.relu(self.hidden1(x))
        x = self.relu(self.hidden2(x))
        x = self.output(x)
        return x

# 3.model,loss func,optimizer
model = main()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
epochs = 500
for epoch in range(epochs):
    pred = model(X_train)
    loss = criterion(pred, y_train)
    optimizer.zero_grad() 
    loss.backward()      
    optimizer.step()     
    if (epoch + 1) % 50 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')
model.eval()
with torch.no_grad():
    # Quãng đường 5km, 3 đèn đỏ, tắc đường 4, thời tiết 2
    test_input = torch.tensor([[5.0, 3.0, 4.0, 2.0]])
    predicted_time = model(test_input)
    print(f'\nDự đoán cho [5km, 3 đèn, kẹt xe mức 4, thời tiết mức 2]: {predicted_time.item():.2f} phút')

