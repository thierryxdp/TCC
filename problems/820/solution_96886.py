def posLetra(frase, letra, ocorrencia):
    """função que recebe uma string, uma letra, e um número que indica a ocorrencia da letra e retorna a posição em que a ocorrencia da letra está,
	caso exista menos ocorrencias do que pedido, retorna -1
	str, str, int -> int"""

    posicao = frase.find(letra)
    
    while posicao >= 0 and ocorrencia > 1:
        posicao = frase.find(letra, posicao + 1)
        ocorrencia -= 1
	
    return posicao