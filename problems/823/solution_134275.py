def faltante(lista):
    a=1
    b=0
    while a<len(lista):
        if lista[a]-lista[a-1]!=1:
            b=lista[a-1]+1
        a=a+1
    return b