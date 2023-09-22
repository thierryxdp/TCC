def faltante(lista):
    
    list.sort(lista)
    posicao=0
    
    if lista[-1]!=len(lista):
        return len(lista)+1
    
    
    while lista[posicao]==lista[posicao+1]-1:
        posicao=posicao+1
        
    return lista[posicao]+1