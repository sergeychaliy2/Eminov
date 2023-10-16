import random
import tkinter as tk

# Создаем функцию для моделирования
def simulate_uniform_distribution():
    a = float(a_entry.get())
    b = float(b_entry.get())
    N = int(N_entry.get())

    xi_list = [b + random.random() * (a - b) for _ in range(N)]

    M = (b + a) / 2
    D = (a - b) ** 2 / 12

    m = (1 / N) * sum(xi_list)
    g = (1 / (N - 1)) * sum([xi ** 2 for xi in xi_list]) - \
        (N / (N - 1)) * m ** 2

    # Создаем окно для вывода результатов
    result_window = tk.Toplevel(root)
    result_window.title('Результаты моделирования')
    result_window.geometry('300x200')

    # Создаем и настраиваем элементы интерфейса в окне результатов
    result_label = tk.Label(result_window, text=' ===== MODELING RESULT =====\n'
                                                f'M = {M}\n'
                                                f'D = {D}\n'
                                                f'|M - m| = {abs(M - m)}\n'
                                                f'|D - g| = {abs(D - g)}',
                            justify='left')
    result_label.pack()

# Создаем главное окно
root = tk.Tk()
root.title('Моделирование равномерного распределения')
root.configure(bg='white')

# Создаем и настраиваем элементы интерфейса
a_label = tk.Label(root, text='a = ', bg='white')
b_label = tk.Label(root, text='b = ', bg='white')
N_label = tk.Label(root, text='N = ', bg='white')
a_entry = tk.Entry(root)
b_entry = tk.Entry(root)
N_entry = tk.Entry(root)
simulate_button = tk.Button(root, text='Моделировать', command=simulate_uniform_distribution, bg='blue', fg='white')

# Размещаем элементы на главном окне
a_label.pack()
a_entry.pack()
b_label.pack()
b_entry.pack()
N_label.pack()
N_entry.pack()
simulate_button.pack()

# Запускаем главное окно
root.mainloop()
