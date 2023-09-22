def eh_quadrada(mo):
    """identifica se a matriz de entrada é quadrada.
    list->bool"""
    if mo==[]:
        return True
    else:
        return len(mo)==len(mo[0])