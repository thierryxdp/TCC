def eh_quadrada(matriz):
    """retorna se uma matriz é quadrada ou não
       matriz->str"""
    if len(matriz)==0:
        return "True"
    elif len(matriz)==len(matriz[0]):
        return "True"
    else:
        return "False"