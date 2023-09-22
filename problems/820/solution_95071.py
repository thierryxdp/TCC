def posLetra(string, letra, numero):
    """Função que recebe uma string, uma letra e um numero que indica a ocorrencia
    desejada da letra e retorna em que posição da string essa ocorrencia da letra
    está. Caso exista menos ocorrencias da letra do que a ocorrencia pedida, a 
    função retorna -1.
    str, str, int -> int."""
    inicio = 0
    indice = 0
    posicao = str.find(string, letra, inicio)  
    while indice < numero:        
        indice = indice + 1
        inicio = posicao + 1
	return posicao