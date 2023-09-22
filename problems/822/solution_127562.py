def repetidos (numeros):
    ''' função que retorna a quantidade de vezes que números se repetiram na lista
    list->int'''
    
    i=1
    contador = 0 
    
    while i<len(numeros):
        if numeros [i] == numeros [i-1]:
            contador = contador + 1
    return contador