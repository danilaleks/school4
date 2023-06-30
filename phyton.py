import pandas as pd

# Прочитати файл з оцінками у DataFrame
df = pd.read_csv('grades.csv')

# Обчислити середнє значення оцінки по групі
group_avg = df.groupby('Group')['Grade'].mean()

# Вивести середнє значення оцінки по групі
print("Середнє значення оцінки по групі:")
print(group_avg)
print()

# Обчислити середнє значення оцінки по всіх студентах
overall_avg = df['Grade'].mean()

# Вивести середнє значення оцінки по всіх студентах
print("Середнє значення оцінки по всіх студентах:", overall_avg)
print()

# Вивести імена студентів, оцінка яких вище середньої
above_avg_students = df[df['Grade'] > overall_avg]['Name']

print("Імена студентів з оцінками вище середньої:")
for name in above_avg_students:
    print(name)
