# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_data(data):
#     # مخطط البيانات المنتشرة (Scatter plot) بين عمودي radius_mean و texture_mean
#     plt.scatter(data['radius_mean'], data['texture_mean'])
#     plt.xlabel('Radius Mean')
#     plt.ylabel('Texture Mean')
#     plt.title('Scatter Plot')
#     plt.show()

#     # مخطط البيانات الشريطية (Bar plot) لعدد الأورام الخبيثة والحميدة
#     diagnosis_counts = data['diagnosis'].value_counts()
#     plt.bar(diagnosis_counts.index, diagnosis_counts.values)
#     plt.xlabel('Diagnosis')
#     plt.ylabel('Count')
#     plt.title('Bar Plot')
#     plt.show()

#     # مخطط الكثافة (Histogram) لعمود radius_mean
#     plt.hist(data['radius_mean'], bins=20)
#     plt.xlabel('Radius Mean')
#     plt.ylabel('Frequency')
#     plt.title('Histogram')
#     plt.show()

# def main():
#     # قراءة ملف CSV
#     data = pd.read_csv("ResultCleaningData/data.csv")

#     # عرض البيانات في المخططات
#     plot_data(data)

# if __name__ == "__main__":
#     main()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(data):
    # مخطط نسبة الأورام الخبيثة والحميدة باستخدام Pie chart
    # diagnosis_counts = data['diagnosis'].value_counts()
    diagnosis_counts = data['diagnosis'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(diagnosis_counts, labels=diagnosis_counts.index, autopct='%1.1f%%')
    plt.title('Diagnosis Distribution')
    plt.show()

    # مخطط العلاقة بين عمودي radius_mean و texture_mean باستخدام Scatter plot مع تلوين حسب التشخيص
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='radius_mean', y='texture_mean', hue='diagnosis', palette='Set1')
    plt.xlabel('Radius Mean')
    plt.ylabel('Texture Mean')
    plt.title('Scatter Plot with Diagnoses')
    plt.show()

    # مخطط Box plot لعمودي radius_mean و texture_mean مع تلوين حسب التشخيص
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data, x='diagnosis', y='radius_mean', palette='Set1')
    plt.xlabel('Diagnosis')
    plt.ylabel('Radius Mean')
    plt.title('Box Plot of Radius Mean with Diagnoses')
    plt.show()

def main():
    # قراءة ملف CSV
    data = pd.read_csv("CleaningData/data.csv")

    # عرض البيانات في المخططات
    plot_data(data)

if __name__ == "__main__":
    main()