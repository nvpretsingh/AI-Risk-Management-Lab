# Modify a fraud input slightly to test robustness
X_test_adv = X_test.copy()
X_test_adv.iloc[0] *= 1.01  # Slight manipulation

# Predict again with modified input
y_pred_adv = model.predict(X_test_adv)
print(f"Original prediction: {y_pred[0]}, Adversarial prediction: {y_pred_adv[0]}")