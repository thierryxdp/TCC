def repetidos(lista):
    '''Funcao que recebe como entrada uma lista de numeros.
    E retorna o numero de vezes que um elemento da lista e igual ao elemento anterior.
    list -> int'''
    
    i = 0
    recorrencia = 0
    
    while i < len(lista) - 1:
        if lista[i] == lista[i+1]:
            recorrencia += 1
        i += 1
        
    return recorrencia