def repetidos(lista):
    list.sort(lista)
    i = 0
    repetidos = 0
    
    if lista[i] != lista[i+1]:
        i+=1
        else:
            i+=2 and repetidos +=1
            
    return repetidos