
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.core import tools

#trong đây t draft thôi, hiện chỉ có biến purchase amount
#mng tạo file làm theo phân công rồi commit push lên nha
file = r'D:\DATASET\Fashion_Store_Data_Analysis.xlsx'
df = pd.read_excel(file, sheet_name='Fashion_Store_Data')


'''print(df['Age'].describe())

# Kiểm tra giá trị bị thiếu
print(df['Age'].isnull().sum())

# Kiểm tra độ lệch và độ nhọn
print("Skewness:", df['Age'].skew())

plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Histogram of Purchase Amount (USD)")
plt.xlabel("Age")
plt.ylabel("count")
plt.show()

#Vẽ Boxplot Để Phát Hiện Outliers
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Age'])
plt.title("Boxplot of Age")
plt.show()

#Xử Lý Outliers (Loại Bỏ Giá Trị Ngoại Lệ)
# Tính IQR (Interquartile Range)
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# Xác định ngưỡng outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Lọc dữ liệu, loại bỏ outliers
df_cleaned = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

# Kiểm tra lại thống kê mô tả sau khi loại bỏ outliers
print(df_cleaned['Age'].describe())'''

# Tạo figure với 2 cột, 2 hàng để hiển thị Histogram và Box Plot
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histogram cho Age
sns.histplot(df["Age"], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Histogram of Age")

# Histogram cho Quantity
sns.histplot(df["Qty"], bins=10, kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Histogram of Quantity")

# Box Plot cho Age
sns.boxplot(y=df["Age"], ax=axes[1, 0])
axes[1, 0].set_title("Box Plot of Age")

# Box Plot cho Quantity
sns.boxplot(y=df["Qty"], ax=axes[1, 1])
axes[1, 1].set_title("Box Plot of Quantity")

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
