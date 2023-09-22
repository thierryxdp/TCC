def posLetra (string, letra, ocorrencia):
	"""Função que irá recceber como entrada uma string, uma letra e um número que indica a ocorrência desejada da letra. A função irá retornar em que posição da string aquela ocorrência da letra esté.
    
    	Parameters:
        string: frase que será analisada
        letra: letra que será procurada dentro da string
        ocorrencia: ocorrência desejada da letra na string
        
        Returns:
        posição da letra dentro da string. Caso exista menos ocorrência do que o solicitado, retornará -1
    """

    posicao = 0
    posicaodaletra = []
    while posicao < len(string):
		if str.upper(string[posicao]) in str.upper(letra):
            posicaodaletra += [posicao]
        i = i + 1
    if len(posicaodaletra) < ocorrencia:
        return -1
    else: 
        return posicaodaletra[ocorrencia -1]