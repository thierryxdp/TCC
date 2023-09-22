def filtraMultiplos(lista, n):
    i=0
    l_final=[]
    while i<len(lista):
        if lista[i]%n==0:
            l_final.append(lista[i])
        i++
    return l_final