def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tup->tup'''
    len(a)==4
    erro=','
    if a[0]%2==0:
        return a[0]+erro
    elif a[1]%2==0:
        return [1]+erro
    elif a[2]%2==0:
        return a[2]+erro
    elif a[3]%3==0:
        return a[3]+erro
    else:
        return()