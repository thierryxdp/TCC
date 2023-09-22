def eh_quadrada(matriz):
    """Calcula e retorna se a matriz eh quadrada, sem nenhuma linha, nem coluna; list--> bool"""
    termos=True
    for i in matriz:
        for j in i:
            if j != 0:
                termos=False
    return termos