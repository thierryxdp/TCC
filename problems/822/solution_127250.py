def repetidos(lista):
    """Essa função retorna quantas vezes em uma lista,
    um numero e igual anterior
    lista->int"""
    
    i = 0
    j = 0
    
    while i<len(lista):
        
        if lista[i] == lista[i-1]: #compara um indice com o anterior
            j+=1
        i+=1
    
    return j