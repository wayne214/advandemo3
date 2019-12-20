from tkinter import *


# # 创建Tk对象，Tk代表窗口
# root = Tk()
# # 设置窗口标题
# root.title('窗口标题')
# # 创建Label对象， 第一个参数指定该Label放入root
# w = Label(root, text='Hello Tkinter!')
# # 调用pack进行布局
# w.pack()
# # 启动主窗口的消息循环
# root.mainloop()

class App:
    def __init__(self, master):
        self.master = master
        self.initWidget()

    def initWidget(self):
        # 创建第一个容器
        fm1 = Frame(self.master)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向fm1中添加3个按钮
        # 设置按钮从顶部开始排列，且按钮只能在水平（X）方向填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第三个').pack(side=TOP, fill=X, expand=YES)
        # 创建第二个容器
        fm2 = Frame(self.master)
        # 该容器放在左边排列，就会挨着fm1
        fm2.pack(side=LEFT, padx=10, expand=YES)
        # 向fm2中添加3个按钮
        # 设置按钮从右边开始排列
        Button(fm2, text="第一个").pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text="第二个").pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text="第三个").pack(side=RIGHT, fill=Y, expand=YES)

        # 创建第三个容器
        fm3 = Frame(self.master)
        # 该容器放在右边排列，就会挨着fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        # 向fm3中添加3个按钮
        # 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向填充
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES)


root = Tk()
root.title('PACK布局')
display = App(root)

root.mainloop()
