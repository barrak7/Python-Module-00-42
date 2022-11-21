import sys

i = len(sys.argv)
if i == 1:
    print("Usage: python operations.py <n1> <n2>\nExample:\n\tpython operations.py 10 5")
    sys.exit()
elif i < 3:
    raise AssertionError("too few arguments")
    sys.exit()
elif i > 3:
    raise AssertionError("too many arguments")
    sys.exit()
elif (sys.argv[1].isnumeric() == False) or (sys.argv[2].isnumeric() == False):
    raise AssertionError("only integers")
    sys.exit()
a = int(sys.argv[1])
b = int(sys.argv[2])
print("Sum:         ", a + b)
print("Difference:  ", a - b)
print("Product:     ", a * b)
if (b == 0):
    print("Quotient:    ERROR (division by zero)")
    print("Remainder:   ERROR (modulo by zero)")
else:
    print("Quotient:    ", a / b)
    print("Remainder:   ", a % b)
