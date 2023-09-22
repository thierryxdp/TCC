def carros(n,c=5):
    if n<=c:
        return 1
    elif n>c:
        return math.ceil(n/c)