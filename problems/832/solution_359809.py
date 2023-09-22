def eh_quadrada(m):
    if len({len(i) for i in m}) > 1:
        linhas = len(m)
        colunas = len(m[0])
    	if linhas == colunas:
    		return True
    	else:
    		return False