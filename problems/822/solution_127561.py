def repetidos (numeros):
    ''' função que retorna a quantidade de vezes que números se repetiram na lista
    list->int'''
    
    i=0
    contador = 0 
    
    while i<len(numeros):
        if i!=0:
            if numeros [i] == numeros [i-1]:
                contador = contador + 1
        else:
            contador = contador+0
    return contador