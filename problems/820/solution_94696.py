def posLetra(string,letra,num):
    i=0
    lista=[]
    
    if string.count(letra)<num:
        return -1
    
    while i<len(string):
        if string [i] == letra:
            lista = lista + [i]
            
        i = i+1
        
    resultado = lista[num-1]
    
    return resultado