## 🕶️ THE PHISHINATOR

> *Click if you dare. I’ll be waiting.*

**The Phishinator** is an AI-powered web application that analyzes URLs and detects whether they're phishing or legitimate using machine learning and handcrafted feature engineering.

---

### 🧠 Features

* ⚡ Real-time phishing detection
* 🤖 AI model trained on 800k+ labeled URLs
* 🔎 Feature-based classification using URL structure
* 🧪 Interactive web UI built with React
* 📈 91% accuracy on test data
* ☣️ The Terminator-inspired theme

---

## 🛠️ Tech Stack

| Part     | Tech                        |
| -------- | --------------------------- |
| Backend  | Python, Flask, scikit-learn |
| Frontend | React, CSS                  |
| ML Model | Random Forest Classifier    |
| Extras   | Flask-CORS, Joblib, Pandas  |

---

## 🚀 Quick Start

### 📦 1. Clone the Repo

```bash
git clone https://github.com/yourusername/the-phishinator.git
cd the-phishinator
```

---

### 🧪 2. Backend Setup (Flask API)

```bash
cd api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r ../requirements.txt
```

> ✅ Make sure the file `models/phishing_model.pkl` exists (you can retrain using `main.py` if needed).

#### ▶️ Run Flask server

```bash
python app.py
```

By default, it runs at `http://localhost:5000`.

---

### 💻 3. Frontend Setup (React)

```bash
cd ../the-phishinator
npm install
npm run start
```

Runs on `http://localhost:3000` and connects to the Flask API.

---

## 📊 Model Performance

| Metric    | Value           |
| --------- | --------------- |
| Accuracy  | 91%             |
| Precision | 0.93 (phishing) |
| Recall    | 0.88 (phishing) |
| F1-score  | 0.91            |

---

## 📁 Project Structure

```
.
├── api/                 → Flask backend
│   └── models/          → Saved ML model (pkl)
│   └── app.py
├── the-phishinator/     → React frontend
├── data/                → Raw CSV dataset
├── src/                 → ML pipeline code
│   ├── __init__.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── predict.py
│   └── utils.py
├── .gitignore
├── README.md
├── __init__.py
├── main.py              → Run training + evaluation
└── requirements.txt

```

---

## 🧠 Future Improvements

* [ ] Integrate XGBoost or deep learning models
* [ ] Deploy backend & frontend (e.g. with Docker)
* [ ] Add user feedback & URL reporting
* [ ] Scan full HTML/JS page (not just URL)

---

## 🛡️ Disclaimer

This tool is intended for educational and security research purposes. No guarantees are made about prediction accuracy for real-world websites. Always verify results independently.

---

## 📬 Contact

Built with 💥 by **Omar Chiboub**
[LinkedIn](https://www.linkedin.com/in/omar-chiboub/) | [GitHub](https://github.com/R4M-0)

