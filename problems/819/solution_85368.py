def filtraMultiplos(lista, n):
    tam=len(lista)
    cont=0
    multiplos=[]
    
    while cont<len:
        if lista[cont]%n==0:
            multiplos=multiplos+lista[cont]
           
    return multiplos