def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tup->tup'''
    len(a)==4
    um=a[0]%2==0
    dois=a[1]%2==0
    tres=a[2]%2==0
    quat=a[3]%2==0
    if um and dois and tres and quat:
        return a[0:]
    elif um and dois and tres:
        return a[0:2]
    elif um and dois:
        return a[0:1]
    elif um:
        return a[0]
    else:
        return()