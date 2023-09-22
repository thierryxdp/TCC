def qtd_divisores (n):
    i = ()
    for d in n:
        if d%n==0:
            i=i+d
    return i