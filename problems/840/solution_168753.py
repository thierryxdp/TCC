def Bolos(a,b,c):
    """Tem como objetivo calcular a quantidade de bolos
    que João quer fazer dado um número de ingredientes
    int, int, int> int"""
    bolos=0
    while (a>=2) and (b>=3) and (c>=5):
        a = a-2
        b = b-3
        c = c-5
        bolos=bolos+1
    return bolos