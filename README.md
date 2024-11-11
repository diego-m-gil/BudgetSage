# BudgetSage - Personal Finance Categorizer and Analyzer

## TL;DR
**BudgetSage** is a Dockerized solution for categorizing and analyzing personal financial transactions. Using SQLite for data storage and a Hugging Face LLM for text classification, BudgetSage imports financial data from CSV files, categorizes expenses and incomes, and allows interactive querying of your finances. This project is fully automated for repeat use, allowing you to monitor your financial habits over time. Open-source and customizable.

---

## Why?
Tracking finances manually can be tedious. With BudgetSage, you can use AI to automatically categorize transactions and interact with your financial data in plain language.

---

## 🔧 Tech Stack
- **Python 3.10**: Core runtime.
- **SQLite**: Lightweight database to store transactions.
- **Hugging Face Transformers**: Leverages a pre-trained LLM for categorization.
- **Docker & Docker Compose**: Ensures isolated, reproducible environments.

---

## 🧠 What This Script Does
- **Imports CSV Files**: Automatically imports transaction data from CSV files.
- **Categorizes Transactions**: Uses a combination of keywords and an LLM model to assign categories.
- **Interactive Categorization**: If uncertain, prompts the user to confirm categories, remembering preferences for future transactions.
- **Stores Data in SQLite**: Data is saved to a database, allowing for easy querying and persistent storage.

---

## 🚀 Setting It Up

### Clone the Repository
```bash
git clone https://github.com/yourusername/BudgetSage.git
cd BudgetSage
```

Install Dependencies and Build Docker Containers
```bash
docker-compose up -d --build
```

Folder Structure
Ensure you have your CSV files in a csv_files directory within the data folder:
```bash
BudgetSage/
├── data/
│   ├── financial_data.db  # Auto-generated SQLite database
│   └── csv_files/         # Place your CSV files here for automatic import
└── ...
```

### ⚙️ How It Works - Under the Hood
- Data Import: Reads CSV files placed in data/csv_files and stores transactions in SQLite.
- Categorization: Assigns categories based on description keywords and an LLM for accurate classification.
- Interactive Confirmation: Prompts you to confirm categories for ambiguous transactions.
- Memory Storage: Remembers previous categorization choices to apply consistently over time.
- Avoiding Duplicate Imports
- To prevent re-importing the same data, BudgetSage generates a unique hash for each transaction row, ensuring only unique rows are stored.

### 📦 Project Files
- BudgetSage_Categories.py: Handles categorization of transactions.
- Dockerfile.llm: Sets up the LLM environment.
- Dockerfile.sqlite: Sets up SQLite.
- docker-compose.yml: Configures multi-container setup.
- README.md: Project overview and setup instructions (this file).

### 🌍 Contributing
1. Fork the repository.
2. Clone locally.
3. Create a feature branch: git checkout -b feature-branch.
4. Commit your changes.
5. Push to your branch and create a Pull Request.

