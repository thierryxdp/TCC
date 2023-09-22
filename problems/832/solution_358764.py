def eh_quadrada(matriz:list)-> bool:
    """Função que, dada uma matriz,
    retorna true, caso seja quadrada, ou false,
    senão for quadrada."""

    linhas = len(matriz)
    colunas = len(matriz[0])
    
    return linhas == colunas