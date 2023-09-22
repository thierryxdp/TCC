def repetidos(lista):
    list.sort(lista)
    i = 0
    repetidos = 0
    
    while i <= len(lista) :
        if lista[i] == lista[i]:
            i+=1
        else:
            i+=2 
            
    return repetidos