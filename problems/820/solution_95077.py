def posLetra(string, letra, numero):
    """Função que recebe uma string, uma letra e um numero que indica a ocorrencia
    desejada da letra e retorna em que posição da string essa ocorrencia da letra
    está. Caso exista menos ocorrencias da letra do que a ocorrencia pedida, a 
    função retorna -1.
    str, str, int -> int."""
    posicao = 0
    indice = 0
    posicao = str.find(string, letra, posicao) 
    while indice < numero:
        if posicao < 0:
            return -1
        posicao = str.find(string, letra, posicao + 1)
        indice += 1
	return posicao