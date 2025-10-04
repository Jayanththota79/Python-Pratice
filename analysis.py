import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('supermarket_sales.csv')
print(df.head())

# Total sales by city
city_sales = df.groupby('City')['Total'].sum().reset_index()
print("\nTotal Sales by City:")
print(city_sales)

sns.barplot(x='City', y='Total', data=city_sales)
plt.title('Total Sales by City')
plt.show()

# Average sales by gender
gender_sales = df.groupby('Gender')['Total'].mean().reset_index()
print("\nAverage Sales by Gender:")
print(gender_sales)

sns.barplot(x='Gender', y='Total', data=gender_sales)
plt.title('Average Sales by Gender')
plt.show()

# Payment method distribution
sns.countplot(x='Payment', data=df)
plt.title('Payment Method Distribution')
plt.show()


# analyze the data and give the output according to the customers  
# Data Can perdict the sales and sto ck all  thing