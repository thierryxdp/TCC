def filtraMultiplos(lista,n):
    divisiveis=[]
    indice=0
    while indice < len(lista):
        if  lista[indice] % n == 0 :
            divisiveis= divisiveis +[lista[indice]]
        indice=indice + 1  
        
    return divisiveis