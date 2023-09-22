def repetidos(lista):
    '''
    funcao que recebe uma lista
    e retorna o numero de vezes que um elemento da lista
    e igual ao elemento anterior
    list -> int
    '''
    
    i = 0
    
    while i < len(lista):
        
        
        if lista[i] == lista[i+1]:
            i+1
            
        else:
            i = i 
            
        return i