# Simulate Model Drift by Slightly Altering Input Data
X_test_drifted = X_test.copy()
X_test_drifted *= np.random.uniform(0.95, 1.05, X_test.shape)  # Introduce slight variation

# Predict on drifted data
y_pred_drifted = model.predict(X_test_drifted)

# Compare Accuracy Before & After Drift
accuracy_drifted = accuracy_score(y_test, y_pred_drifted)
print(f"Accuracy before drift: {accuracy:.2f}, After drift: {accuracy_drifted:.2f}")

# If accuracy drops significantly, retraining is needed
if accuracy_drifted < 0.80:
    print("Model Drift Detected! Retraining required.")