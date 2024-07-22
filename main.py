import pandas as pd

data = {
    'Имя': ['Петр', 'Нина', 'Владимир', 'Елизавета', 'Дмитрий', 'Виктория', 'Михаил', 'Ольга', 'Павел', 'Василиса'],
    'Математика': [4, 5, 4, 5, 2, 4, 3, 5, 3, 4],
    'География': [4, 5, 3, 5, 2, 5, 3, 4, 2, 5],
    'Теория вероятности': [5, 5, 4, 4, 2, 4, 4, 5, 2, 4],
    'Физика': [5, 4, 2, 3, 5, 4, 4, 5, 3, 2],
    'Русский язык': [5, 5, 5, 2, 4, 4, 3, 5, 4, 5]
}

df = pd.DataFrame(data)

numeric_df = df.select_dtypes(include=['number'])

# Средняя оценка
average_scores = numeric_df.mean()
print("Средняя оценка по каждому предмету:")
print(average_scores)

# Медианная оценка
median_scores = numeric_df.median()
print("Медианная оценка по каждому предмету:")
print(median_scores)

# Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"Q1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}")
print(f"IQR для оценок по математике: {IQR_math}")

# Стандартное отклонение
std_dev = numeric_df.std()
print("Стандартное отклонение по каждому предмету:")
print(std_dev)