def faltante(lista):
    
    peca= [len(lista)] + [1]
    lista.sort()
    i=0
    
    while i<var:
        if peca[i] not in lista:
            return peca[i]
        
        elif lista[i]!=i+1:
            return peca[i]
        else:
            return i+1
        
        i = i+1