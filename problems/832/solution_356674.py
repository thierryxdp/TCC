def eh_quadrada (matriz):
    '''Função diz se a matriz fornecida é quadrada ou não.
    list -> bolean'''
    linhas = len (matriz)
    for i in range (linhas):
        if (len (matriz[i])) != linhas:
            return False
    return True