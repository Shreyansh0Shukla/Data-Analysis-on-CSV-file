# Data Analysis on Titanic Dataset

## 📌 Project Overview
This project performs **data analysis** on the Titanic dataset using **Python, Pandas, and Seaborn**. It includes:
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Visualizing Survival Rates Based on Passenger Class
- Handling Missing Data

## 🛠 Technologies Used
- **Python** (pandas, seaborn, matplotlib, numpy)
- **Jupyter Notebook / GitHub Codespaces**
- **Kaggle API** (for dataset download)

## 📂 Dataset
We use the **Titanic Dataset** from Kaggle:
- **Source**: [Yasserh Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **Columns include**: PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, Survived

## 🔧 Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Data-Analysis-on-CSV-file.git
   cd Data-Analysis-on-CSV-file
   ```
2. **Install Required Libraries:**
   ```bash
   pip install pandas numpy seaborn matplotlib kagglehub
   ```
3. **Run the Script:**
   ```bash
   python Data_Analysis.py
   ```

## 📊 Exploratory Data Analysis (EDA)
### 1️⃣ Data Preprocessing
- Handle missing values (`Age`, `Embarked`)
- Convert categorical data

### 2️⃣ Data Visualization
- **Passenger Class vs. Survival Rate:**
  ```python
  sns.barplot(x=df['Pclass'], y=df['Survived'], errorbar=None, hue=df['Pclass'], palette='viridis', legend=False)
  ```
- **Age Distribution:**
  ```python
  sns.histplot(df['Age'], bins=30, kde=True)
  ```

## ✅ Results & Insights
- **First-class passengers** had a higher survival rate.
- **Women and children** were more likely to survive.
- **Missing values** were handled using median imputation.

## 📜 License
This project is open-source and free to use.

## 📬 Contact
For queries, contact **your-email@example.com** or visit **your GitHub profile**.

