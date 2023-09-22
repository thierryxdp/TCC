def filtra_pares(dados):
    '''retorna os números pares'''
    if dados[1]%2==0 and dados[0]%2==0 and dados[3]%2==0:
        return dados[1]
    else:
        return''