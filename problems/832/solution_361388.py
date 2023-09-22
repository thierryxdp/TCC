def eh_quadrada(matriz):
    """Primeiramente, verifica se a matriz é vazia, uma vez que verificar se
    o primeiro elemento de uma matriz vazia tem o mesmo tamanho que a matriz resultaria
    em um problema, já que não encontraria o índice necessitado.
    Caso seja vazia retorna True(quadrada), caso não, verifica se o tamanho da
    lista é o mesmo que o do primeiro elemento, ou seja, se possui o mesmo número
    de linhas e colunas, respectivamente. Caso seja o caso, retorna True,
    caso não, retorna False.
    list-> boolean
	"""
	if matriz==[]:
		return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False