def eh_quadrada(m):
    '''Função que dada uma matriz(m), retorna dados booleanos que identifica se essa matriz é quadrada
       matriz->bool'''
    for i, l in enumerate(m):
        if len(l) != len(m):
            return False
        else:
            return True
        for j in range(i):
            if l[j] != m[j][i]:
                return False
    return True