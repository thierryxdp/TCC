def filtraMultiplos(lista, n):
    tam=len(lista)
    cont=0
    mult=[]
    
    while cont<tam:
        if lista[cont]%n==0:
            mult.append(lista[cont])
        cont=cont+1
        
    return mult