def filtra_pares(dados):
    '''retorna os números pares'''
    if dados[0]%2==0 and dados[1]%2==0 and dados[2]%2==0 and dados[3]%==0:
        return dados[0],dados[1],dados[2],dados[3]
    elif dados[0]%2==0 and dados[1]%2==0 and dados[2]%2==0:
        return dados[0],dados[1],dados[2]
    if dados[0]%2==0 and dados[1]%2==0:
        return dados[0],dados[1]
    elif dados[0]%2==0:
        return dados[0]
    else:
        return''