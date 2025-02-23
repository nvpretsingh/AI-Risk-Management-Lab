# Evaluate Bias in Model Predictions
fraud_preds = y_pred[y_test == 1]  # Predictions on actual fraud cases
nonfraud_preds = y_pred[y_test == 0]  # Predictions on non-fraud cases

print(f"Fraud cases detected: {fraud_preds.sum()} / {y_test.sum()}")
print(f"Non-fraud cases detected: {len(nonfraud_preds) - nonfraud_preds.sum()} / {len(y_test) - y_test.sum()}")