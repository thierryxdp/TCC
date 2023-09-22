def filtraMultiplos(lista,n):
    divisiveis=[]
    tamlista=len(lista)
    quant=0
    
    while quant<tamlista:
        if lista[quant]%n==0:
            divisiveis.append(lista[quant])
        quant=quant+1
        
    return divisiveis