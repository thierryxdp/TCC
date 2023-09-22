def repetidos(lista_numeros):
    """retorna o número de vezes que um elemento da lista é igual ao 
       elemento anterior
       list --> string """
	i = 0
    j = 1
    ocorrencia = 0
    
    while i < len(lista_numeros):
    
		if lista_numeros[i] == lista_numeros[j]:
    		ocorrencia += 1
    
    	i += 1
        j = i + 1
    return ocorrencia