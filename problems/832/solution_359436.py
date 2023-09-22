def eh_quadrada(matriz):
    """essa funcao calcula e retorna uma matriz vazia(sem linha e nem coluna);lista->bool"""
    if len(matriz)==0 or len (matriz)==len(matriz[0]):
        return True
    else:
        return False