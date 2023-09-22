def filtra_pares(n):
    '''
    funcao que recebe uma tupla com quatro elementos
    inteiros e retorna outra tupla com quais desses 
    elementos são pares na mesma ordem da original
    tuple->tuple
    '''
    w,x,y,z=n
    par = tuple()
    
    if w%2==0:
        par+=(w, )
    if x%2==0:
        par+=(x, )
    if y%2==0:
        par+=(y, )
    if z%2==0:
        par+=(z, )
        
    return par