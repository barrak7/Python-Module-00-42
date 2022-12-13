import time
from time import sleep

def ft_progress(lst):
    s = time.time()
    i = s
    l = len(lst)
    prev_len = 0
    for e in lst:
        ela = time.time() - s
        i = (time.time() - i) * (l - (lst.index(e) + 1))
        per = (e + 1) / l * 100
        pr = ("ETA: {}s [ {}%][{}] {}/{} | elapsed time {}s".format(round(i, 2), int(per), "="*(int(per / 10))+">"+" "*(int((100 - per) / 10)), e + 1, l, round(ela, 2)))
        lp = len(pr)
        if (prev_len > lp):
            prev_len = prev_len - lp
            print(pr+" "*prev_len, end="\r")
        i = time.time()
        prev_len = lp
        yield e

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.1)
print()
print(ret)
