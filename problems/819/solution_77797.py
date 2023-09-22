def filtraMultiplos(lista,n):
    for indice, valor in enumerate(lista): 
        if ((valor%n)!=0):
            lista.remove(valor)
            indice+=1
    print(lista)
    return