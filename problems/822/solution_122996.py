def repetidos(lista):
    
    """Funçao que recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao elemento 
    anterior"""
    
    contagem = 0
    proximo = 0
    
    while proximo < len(lista) - 1 :
        
        if lista[proximo] == lista[(proximo) + 1]:
            
            contagem = contagem + 1
        proximo = proximo + 1
        
	return contagem