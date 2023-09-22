def primo (n):
    a = []
    for d in range(1, (n+1)):
        if n%d == 0:
            a = a + [n]
        else:
            a = a + []
    return (len(a) == 1) or (len(a) == 2)