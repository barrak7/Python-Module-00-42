kata = (0, 4, 132.42222, 1000, 12345.67)

kata = list(kata)
kata[0] = str(kata[0])
kata[1] = str(kata[1])
print("module_{}, ex_{} : {:.2f}, {:.2e}, {:.2e}".format(kata[0].zfill(2), kata[1].zfill(2), kata[2], kata[3], kata[4]))
