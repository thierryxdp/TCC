def eh_quadrada(numero):
    """Identifique se a matriz é quadrada"""
    i =0
    for x in range(len(numero)):
        i = i + 1
        c = 0
        for j in range(len(numero[0])):
            c = c + 1
            if i == c:
                return True
            if i == 0:
                return True
            else:
                return False