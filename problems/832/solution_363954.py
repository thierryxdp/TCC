def eh_quadrada(m):
    """Código que retorna true se a matriz for quadrada
    e False se não
    :m ---> lista:
    :return --> Bool:
    """
    return True if len(m) == 0 else len(m) == len(m[0])