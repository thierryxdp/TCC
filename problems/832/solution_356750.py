def eh_quadrada(x):
    """Função que identifica se a matriz é quadrada
    list --> bool"""
    matrizvazia= [[]];
    if len(x) == len(x[0]) or x== matrizvazia:
        return True;
    else:
        return False;