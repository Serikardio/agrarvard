import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Загрузка данных из SPSS и сохранение их в Excel для каждого года и страны
def process_data(country, year):
    data = pd.read_spss(f'/content/drive/MyDrive/lab 12/{country}_{year}_FIES_v01_EN_M_v01_A_OCS.sav')
    data.to_excel(f'{country}-{year}.xlsx')

# Загрузка данных из Excel, замена пропущенных значений на 0 и сохранение изменений
def process_excel(country, year):
    df = pd.read_excel(f'/content/drive/MyDrive/lab 12 excel/{country}-{year}.xlsx')
    df.fillna(0, inplace=True)
    df.to_excel(f'/content/drive/MyDrive/lab 12 excel/{country}-{year}.xlsx', index=False)

# Вычисление среднего значения m для каждой страны и каждого года
def calculate_m(country, year):
    df = pd.read_excel(f'/content/drive/MyDrive/lab 12 excel/{country}-{year}.xlsx')
    m = (df['Prob_Mod_Sev'] * df['wt']).sum() / df['wt'].sum()
    return m

# Создание списков средних значений m для каждой страны и каждого года
def create_m_values(country):
    m_values = []
    for year in range(2014, 2018):
        m = calculate_m(country, year)
        m_values.append(m)
    return m_values

# Создание графика для всех стран
def plot_data():
    countries = ['KGZ', 'KZ', 'TJK', 'UZB']
    plt.figure(figsize=(10, 6))
    years = range(2014, 2018)
    for country in countries:
        m_values = create_m_values(country)
        plt.plot(years, m_values, marker='o', linestyle='-', label=country)
    plt.title('Центральная Азия')
    plt.xticks(years)
    plt.yticks(np.arange(0, 0.3, 0.05))
    plt.legend()
    plt.grid(True)
    plt.show()

# Обработка данных для каждой страны и каждого года
for country in ['KGZ', 'KZ', 'TJK', 'UZB']:
    for year in range(2014, 2018):
        process_data(country, year)
        process_excel(country, year)

# Построение графика средних значений m для каждой страны и каждого года
plot_data()
