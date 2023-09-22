def eh_quadrada(numero):
    """Identifique se a matriz é quadrada"""
    i =0
    c = 0
    for x in range(len(numero)):
        i = i + 1
        for j in range(len(numero[0])):
            c = c + 1
            if i == 0:
                return True
            elif i == c:
                return True
            else:
                return False
    else:
        return True