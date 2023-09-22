def repetidos (lista):
    
    lista2=[]
    rep = 0
    i = 0
    while i < len(lista):
        lista2=lista.count(lista[i]) + 1
        i=i+1
        
        return  lista2