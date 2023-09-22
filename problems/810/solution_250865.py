def inverte(x):
    A = x.split("-")
    B = x.split()
    C = B[::-1]
    D = str.join(" ",C)
    return D