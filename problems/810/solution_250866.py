def inverte(x):
    A = x.split("-")
    B = A.split()
    C = B[::-1]
    D = str.join(" ",C)
    return