def faltante(lista):
    i=0
    while lista[i]<len(lista):
        if i+1==lista[i]:
            i +=1
    return i+2