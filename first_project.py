#!/usr/bin/env python
# coding: utf-8

import pandas as pd
#считываю файл изменяю имя колонок в удобный для работы формат
def new_names(name):
    return name.replace(" ", '_').lower()

path_to_file = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-d-tomahin/shared/homeworks/python_ds_miniprojects/2/bookings.csv'
bookings = pd.read_csv(path_to_file, encoding = 'windows-1251', sep = ';')
bookings = bookings.rename(columns = new_names)


#ищу страну из которой больше всего клиентов
bookings.groupby('country').aggregate({"meal":"count"}).sort_values("meal")


#среднее значение ночей проведенных в отеле
bookings.groupby('hotel').aggregate({"stays_total_nights": "mean"}).round(2)


#количество заказов, где тип назначенной комнаты не совпал с зарезервированным
len(bookings.query("assigned_room_type != reserved_room_type"))


#ищу месяц в котором больше всего броней
bookings.query('arrival_date_year == 2017').groupby('arrival_date_month').agg('count').sort_values('hotel', ascending = False)


#ищу месяц, в котором в отеле больше всего отмен
bookings.query('hotel == "City Hotel" & is_canceled == 1')    .groupby(['arrival_date_year', 'arrival_date_month'])    ['arrival_date_month'].value_counts().sort_values(ascending = False)


#считаем среднее число детей, взрослых, и бейбиков
print(bookings['adults'].mean())
print(bookings['children'].mean())
print(bookings['babies'].mean())


#сравниваю среднее число детей между 2 отелями
bookings['total_kids'] = bookings['babies'] + bookings['children']
bookings.groupby('hotel').agg({'total_kids':"mean"}).round(2)
bookings


#сравнить процент отмен между посетителями с детьми и без детей
bookings['has_kids'] = bookings['total_kids'] >= 1
is_canceled_kids = len(bookings.query('has_kids == True & is_canceled == 1'))                       /len(bookings.query('has_kids == True'))
is_candeled_without_kids = len(bookings.query('has_kids == False & is_canceled == 1'))                       /len(bookings.query('has_kids == False'))
print(round(is_canceled_kids * 100 , 2), round(is_candeled_without_kids * 100, 2))




