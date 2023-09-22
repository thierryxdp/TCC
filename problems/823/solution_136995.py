def faltante(lista):
    x=0
    y=1
    while x<len(lista):
        if y not in lista:
            return y
        x=x+1
        y=y+1