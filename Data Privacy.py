from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a sample fraud transaction
sample_transaction = str(X_test.iloc[0].values).encode()
encrypted_transaction = cipher.encrypt(sample_transaction)

print(f"Encrypted transaction: {encrypted_transaction}")

# Decrypt the transaction
decrypted_transaction = cipher.decrypt(encrypted_transaction)
print(f"Decrypted transaction: {decrypted_transaction}")