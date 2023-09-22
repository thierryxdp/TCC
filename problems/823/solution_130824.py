def faltante(lista):
    
    var=len(lista)+1
    lista.sort()
    i=0
    
    while i<var:
        if var[i] not in lista:
            return var[i]
        
        i = i+1