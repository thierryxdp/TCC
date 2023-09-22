def eh_quadrada(m):
    """função que identifica se uma matriz é quadrada, avtravés da matriz m de entrada;
    Entrada: list
    Saída: bool"""
    
    if len (m) == []:
        return True
    if len(m) == len(m[0]):
        return True
    else:
        return False