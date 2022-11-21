import sys

i = 1;
n = len(sys.argv)
if (n == 1):
    sys.exit()
s = " ".join(sys.argv[1::])
s = reversed(s)
s = "".join(s)
print(s)
