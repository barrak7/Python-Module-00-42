kata = (19, 42, 21, 1337)

print("The", len(kata),"numbers are:", end =" ")
for i in kata:
    if (i != kata[-1]):
        print("{}, ".format(i), end ="")
    else:
        print(i)
