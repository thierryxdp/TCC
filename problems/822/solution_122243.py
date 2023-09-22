def repetidos(lista):
    """calcula e retorna o numero de vezes que um elemento da lista
       e igual ao elemento anterior 
       
       lista->int
    """
    
    i = 0 
    repeticoes = 0
    
    while i < len(lista):
        if lista[i] == lista[i+1]:
        i = i +1
        repeticoes = repeticoes +1
        
    return repeticoes