import math
import random
import tkinter as tk
from tkinter import ttk
from tkinter import CENTER

# Функция для моделирования экспоненциального распределения
def simulate_exponential_distribution():
    N = int(N_entry.get())
    L = float(L_entry.get())

    xi_list = [math.log(1 - random.random()) / (-L) for _ in range(N)]

    M = 1 / L
    D = 1 / (L ** 2)

    m = (1 / N) * sum(xi_list)
    g = (1 / (N - 1)) * sum([xi ** 2 for xi in xi_list]) - (N / (N - 1)) * M ** 2

    # Вывод результатов в отдельных колонках
    mx_label.config(text=f'MX = {M}', style="Result.TLabel")
    dx_label.config(text=f'DX = {D}', style="Result.TLabel")
    delta1_label.config(text=f'delta1 = {abs(M - m)}', style="Result.TLabel")
    delta2_label.config(text=f'delta2 = {abs(D - g)}', style="Result.TLabel")

    # Устанавливаем цвета фона для выделения колонок
    mx_label.configure(background='#e6e6e6')
    dx_label.configure(background='#e6e6e6')
    delta1_label.configure(background='#e6e6e6')
    delta2_label.configure(background='#e6e6e6')

# Создаем главное окно
root = tk.Tk()
root.title('Моделирование экспоненциального распределения')

# Установка размера окна и центрирование
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Создаем и настраиваем элементы интерфейса
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), padding=10)
style.configure("Result.TLabel", font=("Helvetica", 12), padding=10, anchor="w")

# Создаем метки для ввода значений
N_label = ttk.Label(root, text='N = ')
L_label = ttk.Label(root, text='lambda = ')
N_label.grid(row=0, column=0, sticky='e')
L_label.grid(row=1, column=0, sticky='e')

# Создаем поля ввода значений
N_entry = ttk.Entry(root)
L_entry = ttk.Entry(root)
N_entry.grid(row=0, column=1, padx=10, pady=10)
L_entry.grid(row=1, column=1, padx=10, pady=10)

# Создаем кнопку для моделирования
simulate_button = ttk.Button(root, text='Моделировать', command=simulate_exponential_distribution, style="TButton")
simulate_button.grid(row=2, column=0, columnspan=2)

# Создаем метки для вывода результатов
mx_label = ttk.Label(root, text='', style="TLabel")
dx_label = ttk.Label(root, text='', style="TLabel")
delta1_label = ttk.Label(root, text='', style="TLabel")
delta2_label = ttk.Label(root, text='', style="TLabel")

# Размещаем метки для вывода результатов
mx_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
dx_label.grid(row=3, column=1, padx=10, pady=10, sticky='w')
delta1_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
delta2_label.grid(row=4, column=1, padx=10, pady=10, sticky='w')

# Запускаем главное окно
root.mainloop()
