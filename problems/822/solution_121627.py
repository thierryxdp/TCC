def repetidos(numeros):
    '''Função recebe uma lista de numeros e retorna o numero de vezes que um 
    elemento da lista é igual ao anterior.
    lista -> int'''
    
    indice = 1
    listadeindices = []
    elemento = numeros[indice]
    anterior = elemento-1
    
    while indice < len(numeros):
        if  elemento == elemento[anterior]:
            listadeindices =+ elemento
            indice = indice+1
    return len(listadeindices)