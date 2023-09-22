def repetidos(lista:list) -> int:
    """Função que irá receber uma lista de números como entrada e irá etornar o número de vezes que um elemento da lista é igual ao elemento anterior.
    
    	Parameters:
        lista: lista com os números que serão analisados
        
        Returns:
        número de vezes que um elemento da lista é igual ao anterior
    """
    
	repeticao = [0]
	posicao = 0
	while posicao < len(lista):
        if lista[posicao] == lista[posicao + 1]:
            repeticao = repeticao + 1
	return repeticao