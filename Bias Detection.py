# Check Fraud vs. Non-Fraud Distribution
fraud_ratio = df['fraud'].value_counts(normalize=True)
sns.barplot(x=fraud_ratio.index, y=fraud_ratio.values)
plt.title("Fraud vs Non-Fraud Cases")
plt.show()