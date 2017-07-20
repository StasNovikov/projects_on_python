# Paint на Python
# Импорт библиотеки
from tkinter import *

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 500
BRUSH_SIZE = 3
COLOR = "black"

# Функция рисования
def paint(event):
    """ Функция рисования """
    global BRUSH_SIZE
    global COLOR

    x1 = event.x - BRUSH_SIZE
    x2 = event.x + BRUSH_SIZE
    y1 = event.y - BRUSH_SIZE
    y2 = event.y + BRUSH_SIZE

    # овал кисти на основе размера brush size, цвет = COLOR, обводка = COLOR
    drawingArea.create_oval(x1,y1,x2,y2,fill=COLOR, outline=COLOR)

# функция смена размера кисти
def brush_size_change(new_size):
    """ функция смена размера кисти """
    global BRUSH_SIZE
    BRUSH_SIZE = new_size

# функция смена цвета кисти
def brush_color_change(new_color):
    """ функция смена цвета кисти """
    global COLOR
    COLOR = new_color


# Создаём окно
root = Tk()
# Создаем заголовок
root.title("Paint на Python")

# Создание области рисования
drawingArea = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")

# Работа мыши
drawingArea.bind("<B1-Motion>", paint)

drawingArea.grid(row=2, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)


# Запуск окна
root.mainloop()