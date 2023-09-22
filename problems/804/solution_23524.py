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
    for par or par1 or par2 or par3 in a:
        return tuple(a)
    else:
        return()