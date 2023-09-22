def faltante(lista):
    a=1
    b=0
    while a<len(lista):
        if lista[a]-lista[a-1]!=1:
            b=lista[a-1]+1
        a=a+1
    if len(lista)==1:
        if lista[0]>1:
            b=lista[0]-1
        else:
            b=lista[0]+1
    if b==0:
        b=a+1
    return b