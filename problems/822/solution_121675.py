def repetidos(lista):
    
    posicao=1
    vezes=[]
    
    while posicao<len(lista):
        if lista[posicao]==lista[posicao-1]:
            list.append(vezes,lista[posicao])
        posicao=posicao+1
        
    return len(vezes)