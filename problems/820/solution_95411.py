def posLetra(frase,letra,n):
    """Funcao que diz a posicao da ocorrencia n da letra na string;
    Entrada: str, str, int
    Saida: int"""

	indice = 0
	listao = []

	if n>str.count(frase, letra):
    	return -1
    while indice < len (frase):
        if frase[indice] == letra:
            list.append(listao, indice)
        indice = indice +1
    return listao[n-1]