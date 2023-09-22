def eh_quadrada(m):
    """Recebe como entrada uma matriz no formato listas de listas e identifica se essa matriz é quadrada ou não através dos valores booleanos 'True' caso seja quadrada e 'False' caso contrário;list->bool"""
    if m==[[]] :
        return True
    elif len(m)==len(m[0]) :
        return True
    else:
        return False