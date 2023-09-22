def eh_quadrada(dic):
    '''Essa função identificar se uma matriz é quadrada'''
    ''' dic -> bool'''
    for i, linha in enumerate(dic):
        if len(linha)!=len(dic):
            return False
        for j in range(i):
            if linha [j]!=dic[j][i]:
                return False
        else:
            return True
    return True