import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



file='D:\DATASET\Fashion_Retail_Sales.xlsx'
df = pd.read_excel (file)
# Thống kê mô tả cho cột Purchase Amount
print(df['Purchase Amount (USD)'].describe())

# Kiểm tra giá trị bị thiếu
print(df['Purchase Amount (USD)'].isnull().sum())

# Kiểm tra độ lệch và độ nhọn
print("Skewness:", df['Purchase Amount (USD)'].skew())

plt.figure(figsize=(8, 5))
sns.histplot(df['Purchase Amount (USD)'], bins=30, kde=True)
plt.title("Histogram of Purchase Amount (USD)")
plt.xlabel("Purchase Amount (USD)")
plt.ylabel("Frequency")
plt.show()