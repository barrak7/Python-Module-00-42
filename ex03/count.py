import string

def text_analyzer(st):
    if st is None:
        st = input("dkhl chi l3ba hna: ")
    if not type(st) is str:
        raise AssertionError("argument is not a string")
    u = 0
    l = 0
    p = 0
    s = 0
    for i in st:
        if i.isupper() == True:
            u += 1
        elif i.islower() == True:
            l += 1
        elif i.isspace() == True:
            s += 1
        elif i in string.punctuation:
            p += 1
    print("- ", u, "upper letter(s)")
    print("- ", l, "lower letter(s)")
    print("- ", p, "punctuation mark(s)")
    print("- ", s, "space(s)")

