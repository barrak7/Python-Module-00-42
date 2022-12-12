import time
from time import sleep

def ft_progress(lst):
    s = time.time()
    i = s
    for e in lst:
        ela = time.time() - s
        i = (time.time() - i) * (len(lst) - (lst.index(e) + 1))
        per = (e + 1) / len(lst) * 100
        pr = ("\rETA: {}s [ {}%][{}] {}/{} | elapsed time {}s".format(round(i, 2), round(per, 2), "="*(int(per / 10))+">"+" "*(int((100 - per) / 10)), e + 1, len(lst), round(ela, 2)))
        print(pr, end="")
        i = time.time()
        yield e

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.1)
print()
print(ret)
