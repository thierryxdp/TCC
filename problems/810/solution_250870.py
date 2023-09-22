def inverte(x):
    A = x.strip("-"), x.strip(",")
    B = A.split()
    C = B[::-1]
    D = str.join(" ",C)
    return A