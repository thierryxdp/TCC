def repetidos (lista):
    '''
    	essa função recebe uma lista de valores e retorna quantas vezes um elemento 
        da lista dada é igual ao seu anterior
        list--> int
    '''
    i=0
    x=0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            x=x+1
        i = i+1
    return x