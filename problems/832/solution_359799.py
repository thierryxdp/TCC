def eh_quadrada(matriz):
    if len({len(i) for i in m}) > 1:
        raise TypeError('Matriz 2D invalida.')
	linhas = len(m)
	colunas = len(m[0]) if linhas else 0
    if linhas == colunas:
    	return True
    else:
    	return False