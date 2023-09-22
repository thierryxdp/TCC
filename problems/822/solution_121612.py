def repetidos(numeros):
    '''Função recebe uma lista de numeros e retorna o numero de vezes que um 
    elemento da lista é igual ao anterior.
    lista -> int'''
    
    i = 0
    listadeindices = []
    
    while i < len(numeros):
        if numeros[indice] == numeros[indice]:
            listadeindices =+ numeros[indice]
       		i = i+1
  	return len(listadeindices)