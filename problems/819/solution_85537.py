def filtraMultiplos(lista, n):
    tamanho=len(lista)
    cont1=0
    multplos=[]
    
    while cont1<tamanho:
        if lista[cont1]%n==0:
            multiplos.append(lista[cont1])
        cont1=cont1+1
        
    return multiplos