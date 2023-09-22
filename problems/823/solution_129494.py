def faltante(lista):
    i=1
    a=0
    while i<len(lista):
        if i==lista[i]:
            i+=1
        elif lista.find(1)==-1:
            a=1
            i+=1
        else:
            a=lista[i]+1
            i+=1
    return a