import sys

n = len(sys.argv)
if (n > 2) == True:
    print("AssertionError: more than one argument are provided")
elif (n < 2) == True:
    sys.exit()
elif not sys.argv[1].isnumeric():
    print("AssertionError: argument is not an integer")
else:
    if (int(sys.argv[1]) % 2) == True:
        print("I'm odd")
    elif int(sys.argv[1]) == 0:
        print("I'm Zero")
    elif (int(sys.argv[1]) % 2) == False:
        print("I'm Even")
