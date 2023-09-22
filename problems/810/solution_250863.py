def inverte(x):
    D = x.split("-")
    A = x.split()
    B = A[::-1]
    C = str.join(" ",B)
    return A