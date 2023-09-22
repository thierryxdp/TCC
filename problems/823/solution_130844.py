def faltante(lista):
    
    peca= [len(lista) + 1]
    lista.sort()
    i=0
    
    while [i]<peca:
        if peca[i] not in lista:
            return peca [i]
        
        elif lista[i]!=i+1:
            return i+1
        else:
            return peca[i] + 1
        
        i = i+1