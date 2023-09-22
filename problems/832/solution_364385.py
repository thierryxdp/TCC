def eh_quadrada(matriz):
    """ Função que identifica se a matriz é quadrada
    Entrada:list
    Saída: bool"""
    linhas = len(matriz) 
    if  linhas == 0:
        return True  
    colunas = len(matriz[0])
    return linhas == colunas