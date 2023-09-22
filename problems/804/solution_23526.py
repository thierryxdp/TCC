def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tuple->tuple'''
    par=a[0]%2==0
    par1=a[1]%2==0
    par2=a[2]%2==0
    par3=a[3]%2==0
    if par in a:
        return a
    else:
        return()