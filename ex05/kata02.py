kata = (2019, 9, 25, 3, 30)

kata = list(kata)
i = 0
n = len(kata)
while (i < n):
    kata[i] = str(kata[i])
    kata[i] = kata[i].zfill(2)
    i = i + 1
print("{}/{}/{} {}:{}".format(kata[1], kata[2], kata[0], kata[3], kata[4]))
