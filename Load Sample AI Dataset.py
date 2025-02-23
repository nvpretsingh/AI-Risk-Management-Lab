import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic fraud dataset
np.random.seed(42)
data_size = 5000
features = 10

X = np.random.rand(data_size, features)
y = np.random.choice([0, 1], size=(data_size,), p=[0.95, 0.05])  # 5% fraud cases

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(features)])
df['fraud'] = y

print("Sample dataset preview:")
print(df.head())