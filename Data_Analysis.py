import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import pandas as pd


path = kagglehub.dataset_download("yasserh/titanic-dataset")

df = pd.read_csv(f"{path}/Titanic-Dataset.csv")

print(df.head())


print(df.info())


df.fillna({'Age': df['Age'].median(), 'Embark_town': 'Unknown'}, inplace=True)


print("\nSummary Statistics:\n", df.describe())
print("\nValue Counts for Passenger:\n", df['Pclass'].value_counts())


plt.figure(figsize=(8, 5))
sns.barplot(x=df['Pclass'], y=df['Survived'], ci=None, palette='viridis')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# Save the cleaned dataset
df.to_csv('cleaned_titanic_data.csv', index=False)
