def filtramutiplos(lista,numero):
    a=[]
    b=0
    while a<len(lista):
        if lista[b]%numero==0:
            a.append(lista[b])
    return a