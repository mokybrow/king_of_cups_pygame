from tkinter import *
import random

root = Tk()
root.geometry('800x500')
root.title('Курсовая работа')


def close():
    root.destroy()


global star
star = 1


def stop():
    global star, rectangle, rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9
    c.delete(rectangle)
    c.delete(rectangle1)
    c.delete(rectangle2)
    c.delete(rectangle3)
    c.delete(rectangle4)
    c.delete(rectangle5)
    c.delete(rectangle6)
    c.delete(rectangle7)
    c.delete(rectangle8)
    c.delete(rectangle9)
    rectangle = c.create_rectangle(10, 20, 40, 50, fill='red')
    rectangle1 = c.create_rectangle(15, 20, 45, 50, fill='red')
    rectangle2 = c.create_rectangle(20, 20, 50, 50, fill='red')
    rectangle3 = c.create_rectangle(30, 20, 60, 50, fill='red')
    rectangle4 = c.create_rectangle(40, 20, 70, 50, fill='red')
    rectangle5 = c.create_rectangle(50, 20, 80, 50, fill='red')
    rectangle6 = c.create_rectangle(60, 20, 90, 50, fill='red')
    rectangle7 = c.create_rectangle(70, 20, 100, 50, fill='red')
    rectangle8 = c.create_rectangle(80, 20, 110, 50, fill='red')
    rectangle9 = c.create_rectangle(90, 20, 120, 50, fill='red')
    star = 0


global count, score
count = 0
score = 0


def click(event):
    global count, score
    x = event.x
    y = event.y

    if (x < c.coords(rectangle)[2] and x > c.coords(rectangle)[0]) and (
            y < c.coords(rectangle)[3] and y > c.coords(rectangle)[1]):
        count += 1

    if (x < c.coords(rectangle1)[2] and x > c.coords(rectangle1)[0]) and (
            y < c.coords(rectangle1)[3] and y > c.coords(rectangle1)[1]):
        count += 1

    if (x < c.coords(rectangle2)[2] and x > c.coords(rectangle2)[0]) and (
            y < c.coords(rectangle2)[3] and y > c.coords(rectangle2)[1]):
        count += 1

    if (x < c.coords(rectangle3)[2] and x > c.coords(rectangle3)[0]) and (
            y < c.coords(rectangle3)[3] and y > c.coords(rectangle3)[1]):
        count += 1
    if (x < c.coords(rectangle4)[2] and x > c.coords(rectangle4)[0]) and (
            y < c.coords(rectangle4)[3] and y > c.coords(rectangle4)[1]):
        count += 1
    if (x < c.coords(rectangle5)[2] and x > c.coords(rectangle5)[0]) and (
            y < c.coords(rectangle5)[3] and y > c.coords(rectangle5)[1]):
        count += 1

    if (x < c.coords(rectangle6)[2] and x > c.coords(rectangle6)[0]) and (
            y < c.coords(rectangle6)[3] and y > c.coords(rectangle6)[1]):
        count += 1
    if (x < c.coords(rectangle7)[2] and x > c.coords(rectangle7)[0]) and (
            y < c.coords(rectangle7)[3] and y > c.coords(rectangle7)[1]):
        count += 1

    if (x < c.coords(rectangle8)[2] and x > c.coords(rectangle8)[0]) and (
            y < c.coords(rectangle8)[3] and y > c.coords(rectangle8)[1]):
        count += 1
    if (x < c.coords(rectangle9)[2] and x > c.coords(rectangle9)[0]) and (
            y < c.coords(rectangle9)[3] and y > c.coords(rectangle9)[1]):
        count += 1
    l2.config(text=count)
    if count == 10:
        score += count
        l4.config(text=score, font='Times 15 bold', fg='gray')
        stop()
        count = 0


def start():
    global dx, dx1, dx2, dx3, dx4, dx5, dx6, dx7, dx8, dx9
    global dy, dy1, dy2, dy3, dy4, dy5, dy6, dy7, dy8, dy9, star
    if star == 1:
        if (c.coords(rectangle)[0] < 1 or c.coords(rectangle)[2] > 700):
            dx = dx * (-1)
        elif (c.coords(rectangle)[1] < 1 or c.coords(rectangle)[3] > 400):
            dy = dy * (-1)

        if (c.coords(rectangle1)[0] < 1 or c.coords(rectangle1)[2] > 700):
            dx1 = dx1 * (-1)
        elif (c.coords(rectangle1)[1] < 1 or c.coords(rectangle1)[3] > 400):
            dy1 = dy1 * (-1)

        if (c.coords(rectangle2)[0] < 1 or c.coords(rectangle2)[2] > 700):
            dx2 = dx2 * (-1)
        elif (c.coords(rectangle2)[1] < 1 or c.coords(rectangle2)[3] > 400):
            dy2 = dy2 * (-1)

        if (c.coords(rectangle3)[0] < 1 or c.coords(rectangle3)[2] > 700):
            dx3 = dx3 * (-1)
        elif (c.coords(rectangle3)[1] < 1 or c.coords(rectangle3)[3] > 400):
            dy3 = dy3 * (-1)

        if (c.coords(rectangle4)[0] < 1 or c.coords(rectangle4)[2] > 700):
            dx4 = dx4 * (-1)
        elif (c.coords(rectangle4)[1] < 1 or c.coords(rectangle4)[3] > 400):
            dy4 = dy4 * (-1)

        if (c.coords(rectangle5)[0] < 1 or c.coords(rectangle5)[2] > 700):
            dx5 = dx5 * (-1)
        elif (c.coords(rectangle5)[1] < 1 or c.coords(rectangle5)[3] > 400):
            dy5 = dy5 * (-1)

        if (c.coords(rectangle6)[0] < 1 or c.coords(rectangle6)[2] > 700):
            dx6 = dx6 * (-1)
        elif (c.coords(rectangle6)[1] < 1 or c.coords(rectangle6)[3] > 400):
            dy6 = dy6 * (-1)

        if (c.coords(rectangle7)[0] < 1 or c.coords(rectangle7)[2] > 700):
            dx7 = dx7 * (-1)
        elif (c.coords(rectangle7)[1] < 1 or c.coords(rectangle7)[3] > 400):
            dy7 = dy7 * (-1)

        if (c.coords(rectangle8)[0] < 1 or c.coords(rectangle8)[2] > 700):
            dx8 = dx8 * (-1)
        elif (c.coords(rectangle8)[1] < 1 or c.coords(rectangle8)[3] > 400):
            dy8 = dy8 * (-1)

        if (c.coords(rectangle9)[0] < 1 or c.coords(rectangle9)[2] > 700):
            dx9 = dx9 * (-1)
        elif (c.coords(rectangle9)[1] < 1 or c.coords(rectangle9)[3] > 400):
            dy9 = dy9 * (-1)

        c.move(rectangle, dx, dy)
        c.move(rectangle1, dx1, dy1)
        c.move(rectangle2, dx2, dy2)
        c.move(rectangle3, dx3, dy3)
        c.move(rectangle4, dx4, dy4)
        c.move(rectangle5, dx5, dy5)
        c.move(rectangle6, dx6, dy6)
        c.move(rectangle7, dx7, dy7)
        c.move(rectangle8, dx8, dy8)
        c.move(rectangle9, dx9, dy9)
        root.after(50, start)
    star = 1


dx = random.randint(-5, 5)
dy = random.randint(-5, 5)
dx1 = random.randint(-5, 5)
dy1 = random.randint(-5, 5)
dx2 = random.randint(-5, 5)
dy2 = random.randint(-5, 5)
dx3 = random.randint(-5, 5)
dy3 = random.randint(-5, 5)
dx4 = random.randint(-5, 5)
dy4 = random.randint(-5, 5)
dx5 = random.randint(-5, 5)
dy5 = random.randint(-5, 5)
dx6 = random.randint(-5, 5)
dy6 = random.randint(-5, 5)
dx7 = random.randint(-5, 5)
dy7 = random.randint(-5, 5)
dx8 = random.randint(-5, 5)
dy8 = random.randint(-5, 5)
dx9 = random.randint(-5, 5)
dy9 = random.randint(-5, 5)

c = Canvas(width=700, height=400, bg='black')
c.place(x=50, y=10)
# Квадраты
rectangle = c.create_rectangle(10, 20, 40, 50, fill='red')
rectangle1 = c.create_rectangle(15, 20, 45, 50, fill='red')
rectangle2 = c.create_rectangle(20, 20, 50, 50, fill='red')
rectangle3 = c.create_rectangle(30, 20, 60, 50, fill='red')
rectangle4 = c.create_rectangle(40, 20, 70, 50, fill='red')
rectangle5 = c.create_rectangle(50, 20, 80, 50, fill='red')
rectangle6 = c.create_rectangle(60, 20, 90, 50, fill='red')
rectangle7 = c.create_rectangle(70, 20, 100, 50, fill='red')
rectangle8 = c.create_rectangle(80, 20, 110, 50, fill='red')
rectangle9 = c.create_rectangle(90, 20, 120, 50, fill='red')


mainmenu = Menu(root)
root.config(menu=mainmenu)

surname = Menu(mainmenu, tearoff=0)
surname.add_command(label="Панин Михаил Сергеевич, группа 20-ИЭ")

helpmenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Об авторе", menu=surname)

# Счёт игры
l1 = Label(text='Счёт:', font='Times 15')
l1.place(x=500, y=430)
l2 = Label(text='0', font='Times 15')
l2.place(x=550, y=430)
l3 = Label(text='Итоговый счёт:', font='Times 15', bg='gray')
l3.place(x=500, y=460)
l4 = Label(text='', font='Times 15')
l4.place(x=640, y=460)
# Кнопка запуска и остановки программы
start_btn = Button(text='Начать', font='Times 15', bg='green', command=start)
start_btn.place(x=50, y=430)
close_btn = Button(text='Выход', font='Times 15', bg='crimson', command=close)
close_btn.place(x=150, y=430)
# Бинд
c.bind('<Button-1>', click)

root.mainloop()
