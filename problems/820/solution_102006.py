def posLetra(frase,letra,ocorrencia):
    """Função que acha a letra desejada na ocorrência desejada na frase. Caso não haja, a função retorna -1"""
    """Parâmetros de entrada:str"""
    """Parâmetros de saída:str"""
    acumulador=0
    indice=0
    while indice<len(frase):
        if frase[indice]==letra:
            acumulador+=1
        	if frase[indice]==letra and acumulador==ocorrencia:
            	return indice
        	else:
            	return -1
        indice+=1