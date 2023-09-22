def carros(n,c=5):
    if n<=c:
        return 1
    elif n>c:
        return round(n/c)
    else:
        return n/c