# Викторина с графическим интерфейсом
# импорт библиотеки
from tkinter import *
from tkinter import messagebox

# рисуем окно
root = Tk()
# Заголовок окна
root.title("Викторина")
# Размеры окна
root.geometry("300x300")

def que_one():
    """ Функция вопроса №1 """
    # Вопрос - Label
    question = Label(root, text="Автор произведения 'Крёстный отец'?")
    # Ответ - Entry - Поле ввода
    answer = Entry(root)
    # Кнопка
    btn = Button(root, text="Ответить", command=lambda: check_the_answer_one(answer))
    # Расположение элементов по строкам, если ставить параметр row=0, row=1 и т.д.
    question.grid()
    answer.grid()
    btn.grid()

def check_the_answer_one(answer):
    """ обработчик нажатия кнопки ответить """
    if answer.get().lower() == "марио пьюзо":
        que_two()
    else:
        messagebox.showerror("Ошибка!","Попробуй ещё раз")

def check_the_answer_two(answer):
    """ обработчик нажатия кнопки ответить """
    if answer.get().lower() == "рафаэль сабатини":
        messagebox.showinfo("Победа","Ты знаток литературы!")
    else:
        messagebox.showerror("Ошибка!","Попробуй ещё раз")

def que_two():
    """ Функция вопроса №2 """
    # Вопрос - Label
    question = Label(root, text="Автор произведения 'Одиссея Капитана Блада'?")
    # Ответ - Entry - Поле ввода
    answer = Entry(root)
    # Кнопка
    btn = Button(root, text="Ответить", command=lambda : check_the_answer_two(answer))
    # Расположение элементов по строкам
    question.grid()
    answer.grid()
    btn.grid()

que_one()

# запуск окна
root.mainloop()