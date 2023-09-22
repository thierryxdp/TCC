def repetidos(numeros):
    '''Função recebe uma lista de numeros e retorna o numero de vezes que um 
    elemento da lista é igual ao anterior.
    lista -> int'''
    
    i = 1
    listadeindices = []
    elemento = numeros[indice]
    
    while i < len(numeros):
        if  elemento == elemento[elemento-1]:
            listadeindices =+ elemento
    	i = i+1
  	return len(listadeindices)