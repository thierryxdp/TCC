def repetidos(lista):
    aux=0
    aux2=0
    lista2=lista[1:len(lista)]
    
    while aux < len(lista2):
        if lista[aux]==lista2[aux]:
            aux2+=1
        aux+=1
    return aux2