def verifica_multiplo(lista,n):
    for indice, valor in enumerate(lista): 
        if ((valor%n)!=0):
            lista.remove(valor)
            indice+=1
    print(lista)
    return





lista=[3,3,3,4,2,11,9]
n=3
verifica_multiplo(lista,n)