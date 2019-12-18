from src.DownUtil import *
import threading

du = DownUtil("http://www.crazyit.org/data/attachment/" \
              + "forum/201801/19/121212ituj1s9gj8g880jr.png", 'a.png', 3)

du.download()


def show_process():
    print('已完成： %.2f' % du.get_complete_rate())
    if du.get_complete_rate() < 1:
        t = threading.Timer(0.1, show_process)
        t.start()


t = threading.Timer(0.1, show_process)
t.start()
