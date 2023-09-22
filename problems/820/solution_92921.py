def posLetra(palavra,letra,ocorrencia):
    '''Função que recebe uma string, uma letra e um numero de ocorrencia 
    desejada para a letra e retorna em que posição da 
    string aquela ocorrência da letra está.
    	str,str,int -> int'''
    
    indice = 0
    posicao = ()
    quantidade = palavra.count(letra)
    
    if letra in palavra:
        if quantidade < ocorrencia:
     		return -1
    while indice < len(palavra):
        if palavra[indice] == letra:
            posicao = posicao + (indice,)
        indice = indice + 1
    return posicao[0:ocorrencia]