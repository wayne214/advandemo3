# grid布局
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidget()

    def initWidget(self):
        # 创建一个输入框组件
        e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
        # 使用pack布局放在最上面
        e.pack(side=TOP, pady=10)
        # 创建一个容器Frame用户包裹下面的按钮
        p = Frame(self.master)
        p.pack(side=TOP)

        # 定义字符串的元组
        names = ("0", "1", "2", "3"
                 , "4", "5", "6", "7", "8", "9"
                 , "+", "-", "*", "/", ".", "=")
        for i in range(len(names)):
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i//4, column=i%4)


root = Tk()
root.title('Grid布局')
display = App(root)

root.mainloop()
