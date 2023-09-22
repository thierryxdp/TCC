def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tuple->tuple'''
    List=[a[0],a[1],a[2],a[3]]
    par= a[0]%2==0 or a[1]%2==0