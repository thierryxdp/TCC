def eh_quadrada(matriz):
    """ Função booleana que identifica se uma matriz é 
        quadrada;
        list(list) -> bool"""
    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])
    if numero_colunas == numero_linhas:
        return True
    else:
        return False