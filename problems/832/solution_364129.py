def eh_quadrada(linhas, colunas):
    """Função que identifica se uma matriz é quadrada ou não,
    e retorna um booleano;
list, list -> bool"""
    if len(linhas) == len(colunas):
        return True
    else:
        return False