
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# قراءة ملف CSV
# data = pd.read_csv("CleaningData/data.csv")
data = pd.read_csv("CleaningData/data.csv", usecols=lambda column: column != 'Unnamed: 32')
# إزالة الأعمدة غير الضرورية






# التحقق من العينة الأولى من البيانات
print(data.head())

# التحقق من الحجم الكلي للبيانات
print(data.shape)

# التحقق من وجود القيم المفقودة في البيانات
print(data.isnull().sum())

# التحقق من الإحصائيات الأساسية للبيانات
print(data.describe())


# التحقق من القيم المكررة في البيانات
print(data.duplicated().sum())




#exectit configrations



columns_to_drop = ["id"]
data = data.drop(columns_to_drop, axis=1)

# تحويل قيمة التشخيص إلى 0 و 1 بدلاً من M و B
diagnosis_mapping = {"M": 1, "B": 0}
data["diagnosis"] = data["diagnosis"].map(diagnosis_mapping)

# معالجة القيم المفقودة
imputer = SimpleImputer(strategy="median")
data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# معالجة القيم المتطرفة
outlier_columns = ["radius_mean", "texture_mean", "perimeter_mean"]
for column in outlier_columns:
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# معالجة المتغيرات الفئوية
categorical_columns = ["diagnosis"]
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# تحويل البيانات باستخدام التدرج القياسي (Standard Scaler)
scaler = StandardScaler()
data.iloc[:, :-1] = scaler.fit_transform(data.iloc[:, :-1])

# تحويل البيانات إلى صيغة نهائية
data.to_csv("ResultCleaningData/data.csv", index=False)