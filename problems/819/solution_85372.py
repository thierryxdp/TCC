def filtraMultiplos(lista, n):
    tam=len(lista)
    cont=0
    multiplos=[]
    
    while cont<tam:
        if lista[cont]%n==0:
            multiplos.append(lista[cont])
        cont=cont+1
        
    return multiplos