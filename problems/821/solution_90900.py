def fatorial(numero):
    i=0
    fat=0
    while 0>=numero:
        if numero%2==0:
            fat=numero/2
        elif numero%3==0:
            fat=numero/3
        elif numero%5==0:
            fat= numero/5
        else:
            fat = numero/7
    return fat