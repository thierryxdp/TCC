def intercala(L1, L2):
    ''''''
    x = L1[:1] + L2[:1]
    y = L1[1:2] + L2[1:2]
    z = L1[2:] + L2[2:]
    return x + y + z