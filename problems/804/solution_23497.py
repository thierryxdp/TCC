def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tup->tup'''
    len(a)==4
    if a[0]%2==0:
        return a[0]
    elif a[1]%2==0:
        return [1]
    elif a[2]%2==0:
        return a[2]
    elif a[3]%3==0:
        return a[3]