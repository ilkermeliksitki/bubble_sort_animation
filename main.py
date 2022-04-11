import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def bubble_sort(ls: np.array) -> None:
    need_next_pass = True
    k = 1
    while k < len(ls) and need_next_pass:
        need_next_pass = False
        for i in range(len(ls) - k):
            if ls[i] > ls[i+1]:
                # swapping 
                ls[i], ls[i+1] = ls[i+1], ls[i]
                yield ls
            need_next_pass = True
        k += 1


def animate(frame, ls):
    plt.cla()
    try:
        old_ls = ls.copy()
        new_ls = next(bubble_sort(ls))
        color_codes = np.array(old_ls == ls, dtype=np.uint)
        color_codes = ["#B20600" if i == 0 else "#00092C" for i in color_codes]
        plt.bar([*range(len(ls))], new_ls, color=color_codes)
        ax = plt.gca()
        ax.axis([0-0.3, np.max(ls)+0.3, 0, np.max(ls)])
    except StopIteration:
        time.sleep(3)
        exit() 

arr = np.arange(15)
np.random.shuffle(arr)
ani = FuncAnimation(fig=plt.gcf(), func=animate, interval=500, fargs=(arr, ))

ax = plt.gca()
ax.set_frame_on(False)
ax.tick_params(left = False, right = False , labelleft = False ,labelbottom = False, bottom = False)
plt.show()
