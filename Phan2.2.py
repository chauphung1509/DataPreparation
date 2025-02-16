import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#trong đây t draft thôi, hiện chỉ có biến purchase amount
#mng tạo file làm theo phân công rồi commit push lên nha

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

#Vẽ Boxplot Để Phát Hiện Outliers
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Purchase Amount (USD)'])
plt.title("Boxplot of Purchase Amount (USD)")
plt.show()

#Xử Lý Outliers (Loại Bỏ Giá Trị Ngoại Lệ)
# Tính IQR (Interquartile Range)
Q1 = df['Purchase Amount (USD)'].quantile(0.25)
Q3 = df['Purchase Amount (USD)'].quantile(0.75)
IQR = Q3 - Q1

# Xác định ngưỡng outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Lọc dữ liệu, loại bỏ outliers
df_cleaned = df[(df['Purchase Amount (USD)'] >= lower_bound) & (df['Purchase Amount (USD)'] <= upper_bound)]

# Kiểm tra lại thống kê mô tả sau khi loại bỏ outliers
print(df_cleaned['Purchase Amount (USD)'].describe())




#LogTransformation
import numpy as np

# Áp dụng log transformation
df['Purchase Amount (USD) Log'] = np.log1p(df['Purchase Amount (USD)'])

# Vẽ lại histogram sau khi log-transform
plt.figure(figsize=(8, 5))
sns.histplot(df['Purchase Amount (USD) Log'], bins=30, kde=True)
plt.title("Histogram of Log Transformed Purchase Amount")
plt.xlabel("Log(Purchase Amount)")
plt.ylabel("Frequency")
plt.show()

