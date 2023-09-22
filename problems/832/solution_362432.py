def eh_quadrada(matriz):
   	"""Funçõ que identifica se a matriz é quadrada.
    matriz->bool"""
    if matriz==[]:
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas!=colunas:
        return False
    else:
        return True