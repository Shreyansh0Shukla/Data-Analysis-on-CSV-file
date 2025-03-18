import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import pandas as pd

# Download the dataset
path = kagglehub.dataset_download("yasserh/titanic-dataset")

# Load CSV file into pandas dataframe
df = pd.read_csv(f"{path}/Titanic-Dataset.csv")

# Display the first few rows
print(df.head())


# Basic info about the dataset
print(df.info())

# Handling missing values
df.fillna({'Age': df['Age'].median(), 'Embark_town': 'Unknown'}, inplace=True)

# Exploratory Data Analysis (EDA)
print("\nSummary Statistics:\n", df.describe())
print("\nValue Counts for Passenger:\n", df['Pclass'].value_counts())

# Visualization: Survival rate by class
plt.figure(figsize=(8, 5))
sns.barplot(x=df['Pclass'], y=df['Survived'], ci=None, palette='viridis')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# Save the cleaned dataset
df.to_csv('cleaned_titanic_data.csv', index=False)
