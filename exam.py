import pandas as pd
import matplotlib.pyplot as plt

data_dict = {
    "Month": ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb"],
    "Total Sales": [5280000, 5501000, 5469000, 5480000, 5533000, 5554000],
    "Target Sales": [5280000, 5500000, 5729000, 5968000, 6217000, 6476000],
    "Advertising Cost": [1056000, 950400, 739200, 528000, 316800, 316800]
}

data = pd.DataFrame(data_dict)

plt.figure(figsize=(10, 4))
plt.plot(data['Month'], data['Total Sales'], marker='o', label='Total Sales', color='blue')
plt.plot(data['Month'], data['Target Sales'], marker='x', label='Target Sales', color='red')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(data['Month'], data['Advertising Cost'], marker='s', label='Advertising Cost', color='green')
plt.xlabel('Month')
plt.ylabel('Ad Costs')
plt.title('Monthly Advertising Costs Trend')
plt.legend()
plt.grid(True)
plt.show()

sales_diff = data['Target Sales'] - data['Total Sales']
plt.figure(figsize=(10, 4))
plt.bar(data['Month'], sales_diff, color='purple')
plt.xlabel('Month')
plt.ylabel('Sales Difference')
plt.title('Difference between Target Sales and Total Sales')
plt.grid(axis='y')
plt.show()
