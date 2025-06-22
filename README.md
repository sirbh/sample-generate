# 📊 PhD Task – Synthetic Data Generation and Evaluation

This project is submitted in response to the PhD application task at BTH, Sweden. It demonstrates the generation, evaluation, and visualization of synthetic tabular data using modern Python tools.

---

## ⚙️ Setup Guide

### ✅ Requirements

- **Python 3.11 or later**

Check your Python version:

```bash
python3 --version
```

### 🐍 Create virtual environment & install dependencies

**Mac/Linux/WSL:**

```bash
python3 -m venv phd-task-env
source phd-task-env/bin/activate
pip install -r requirements.txt
```

**Windows PowerShell:**

```powershell
python3 -m venv phd-task-env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
phd-task-env\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔄 Generate Synthetic Data

To generate new synthetic samples and save them to `synthetic_data.csv`, run:

```bash
python new_samples.py
```

### 📁 Original Data

The original dataset is saved in:

```
dataset.csv
```

It is used as input for training the synthetic data generator.

### 📈 Plot and Analyze

To generate evaluation plots and visualize column-wise or pair-wise distributions, run:

```bash
python plot.py
```

This will help you visually compare the synthetic data with the original.

---


