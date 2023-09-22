def eh_quadrada (x):
    ''' função que indentifica se uma certa matriz é quadrada; dic => bool '''
    for i, linha in enumerate(x):
    if len(linha)!=len(x):
        return False
    for j in range(i): if linha[j]!=x[j][i]: return False
        else:
            return True
        return True