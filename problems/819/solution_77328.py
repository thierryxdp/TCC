def filtraMultiplos(lista,n):
    '''Filtra uma lista, retornando os elementos mutiplos de n da mesma'''
    return [termo for termo in lista if termo %n==0]