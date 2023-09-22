def eh_quadrada (matriz):
    '''Função diz se a matriz fornecida é quadrada ou não.
    list -> bolean'''
    linhas = len (matriz)
    colunas = len (linhas)
    nao_iguais = 0 
    for i in range (linhas):
        if linhas != colunas:
            nao_iguais = nao_iguais +1
    if nao_iguais == 0:
        return True
    else:
        return False