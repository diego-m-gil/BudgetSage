# BudgetSage

Budget Sage - Smart Financial Categorization & Analysis with LLM
TL;DR
Budget Sage is a powerful tool that categorizes and analyzes your financial transactions using Large Language Model (LLM) capabilities. It imports CSV data into an SQLite database, auto-categorizes spending, and can prompt for user input when unsure about certain categories. Built with Python, SQLite, and Docker, it’s designed to automate financial insights while ensuring data privacy.

Why?
Manual financial tracking and categorization is tedious. Budget Sage makes it seamless by combining LLM-based categorization with customizable keyword filters, enabling easy management of personal finances.

🔧 Tech Stack
Python 3.10+: Core language for data processing.
SQLite: Lightweight database to store and query transactions.
Docker & Docker-Compose: Containerized setup for easy deployment.
Transformers (Hugging Face): Utilizes "Nous-Hermes-2-Mistral-7B-DPO" for advanced text-based classification.
🧠 What This Script Actually Does
Budget Sage automatically:

Imports financial transactions from a CSV file.
Runs each transaction description through a categorization pipeline.
Auto-categorizes based on pre-defined keywords and memory for recurring transactions.
Prompts the user when categorization is unclear and remembers future preferences.
Stores the categorized transactions in SQLite for easy querying and analysis.
🚀 Setting It Up
Clone the Repository
First, clone the repository to your environment:

bash
Code kopieren
git clone https://github.com/yourusername/budget-sage.git
cd budget-sage
Install Dependencies
Ensure you’re using Python 3.10+ and install necessary Python packages:

bash
Code kopieren
pip install -r requirements.txt
Configure Environment
Docker Configuration: Edit docker-compose.yml if you need to adjust any environment settings like memory or storage.
WSL Configuration (for Windows): Ensure your WSL has sufficient memory allocated by editing .wslconfig in your user directory.
Prepare CSV Files
Place your CSV files with financial data in the data/csv_files folder. Ensure they follow the expected column structure.

Running the Script
Use Docker to build and run the containers:

bash
Code kopieren
docker-compose up -d --build
This will:

Build the SQLite and LLM containers.
Automatically load your CSV data and start categorizing.
To follow the logs:

bash
Code kopieren
docker-compose logs -f llm
⚙️ How It Works - Under the Hood
Data Import: Imports CSV files into SQLite, skipping duplicates.
Categorization: Combines LLM suggestions with user-defined keyword filtering.
User Prompts: When uncertain, the LLM prompts you for confirmation.
Persistent Memory: Remembers previous categorizations for consistent future labeling.
📦 Project Files
BudgetSage_Categories_0.1.py: Main script for categorizing transactions.
requirements.txt: Lists dependencies.
docker-compose.yml: Docker setup file.
README.md: This file for setup instructions.
.wslconfig: Windows memory configuration (optional).
🌍 Contributing
Want to improve or customize? Fork the repository, create a feature branch, and open a pull request.

📝 License
MIT License. Use, modify, and share freely, with attribution.
