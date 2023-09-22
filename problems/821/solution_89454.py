def fatorial(n):
    """Calcula o fatorial de um número n"""
    i=0
    f=n-i
    fat=1
    while (i< n-1):
        if int(f)>=1:
            fat=fat* f
            i=i+1