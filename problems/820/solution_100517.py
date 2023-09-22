def posLetra(texto, letra, ocorrencia):
    '''Funcao que retorna em que posicao do texto esta a ocorrencia da letra passada
como parametro de entrada. Caso exista menos ocorrencias do que a informada,
a funcao retorna -1.
Str, str, int -> int'''
    posicoes = []
    indice = 0
    if ocorrencia>str.count(texto,letra):
        return -1
    while indice < len(texto):
        if texto[indice] == letra and ocorrencia<=str.count(texto,letra):
            posicoes.append(indice)
        indice = indice + 1
	return posicoes[ocorrencia - 1]