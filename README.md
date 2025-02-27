# AI Risk Management Lab (NIST AI RMF)

This repository provides a **hands-on AI Risk Management Lab** using **AWS SageMaker Studio Lab** and Python. The lab follows the **NIST AI Risk Management Framework (AI RMF)** principles, covering **bias detection, adversarial robustness, data privacy, and model drift monitoring**.

## **📌 Overview**
This project demonstrates AI risk management practices by:
- **Training a Fraud Detection AI Model**
- **Detecting Model Bias**
- **Simulating Adversarial AI Attacks**
- **Encrypting AI Data for Privacy**
- **Monitoring Model Drift for Continuous AI Risk Assessment**

## **📂 Repository Structure**
```
📂 AI-Risk-Management-Lab
│── 📄 AI_Risk.ipynb                                 # Jupyter Notebook with full implementation and documentation
│── 📄 train_AI.py                                   # Python script for training AI model
│── 📄 bias_detection.py                             # Python script for bias analysis
│── 📄 attack_simulation.py                          # Python script for adversarial testing
│── 📄 data_privacy.py                               # Python script for AI data encryption
│── 📄 model_drift.py                                # Python script for detecting model drift
│── 📄 evaluate_bias_in_model_predictions.py         # Python script for evaluating bias in predictions
│── 📄 simulate_ai_governance.py                     # Python script for AI governance simulation
│── 📄 load_sample_AI_Dataset.py                     # Python script for loading dataset
│── 📄 README.md                                     # Documentation (this file)
│── 📄 requirements.txt                              # Required Python libraries
```

---

## **🛠 Setup Instructions**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/nvpretsingh/AI-Risk-Management-Lab.git
cd AI-Risk-Management-Lab
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Jupyter Notebook**
```bash
jupyter notebook
```
Then, open `AI_Risk_Management_Lab.ipynb` and execute each cell step by step.

### **4️⃣ Run Individual Python Scripts**
You can also run specific risk analysis scripts:
```bash
python train_model.py
python bias_detection.py
python adversarial_attack.py
python data_encryption.py
python model_drift.py
python evaluate_bias.py
python simulate_ai_governance.py
python load_sample_dataset.py
```

---

## **📊 AI Risk Management Components**
| **Risk Area**              | **Python Implementation**          | **AWS Equivalent Service** |
|---------------------------|--------------------------------|--------------------------|
| **AI Governance**         | Role-based access simulation   | AWS IAM, CloudTrail       |
| **Bias Detection**        | Fraud data imbalance analysis  | SageMaker Clarify        |
| **Adversarial Attacks**   | Input modification test       | AWS WAF, GuardDuty       |
| **Data Privacy**          | AI data encryption            | AWS Macie, AWS KMS       |
| **Model Monitoring**      | Model drift detection         | SageMaker Model Monitor  |

---

## **🚀 Next Steps**
- [ ] Deploy the AI model in **AWS SageMaker**
- [ ] Automate security with **AWS Lambda**
- [ ] Extend monitoring with **Amazon CloudWatch**


---

## **📝 Author**
Developed by **Navpreet** | https://www.linkedin.com/in/navpreetsingh10/

