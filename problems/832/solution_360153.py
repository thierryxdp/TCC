def eh_quadrada(m):
    """Função que identifica se uma matriz é quadrada.
    list -> bool"""
    if [len(m) == len(m[0])]:
        return True
    elif [[len(m)], [len(m[0])]] == []:
        return True
    else:
        return False