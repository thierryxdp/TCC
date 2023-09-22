def filtra_pares(info):
    '''retorna os elementos pares da tupla original
    tuple->tuple'''
    if info[0,1,2,3]%2==0:
        return (info[0],info[1],info[2],info[3])
    else:
        return ''