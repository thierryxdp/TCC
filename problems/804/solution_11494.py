def filtra_pares(tupla):
    '''Função que recebe uma tupla com quatro
       números inteiros e retorna uma nova 
       tupla apenas com os números pares da 
       original
       tuple -> tuple'''
    
    a = (tupla[0],)
    b = (tupla[1],)
    c = (tupla[2],)
    d = (tupla[3],)
    
    if not tupla[0] == 0:
        a = ()
    if not tupla[1] == 0:
        b = ()
    if not tupla[2] == 0:
        c = ()
    if not tupla[3] == 0:
        d = ()
        
        return a+b+c+d