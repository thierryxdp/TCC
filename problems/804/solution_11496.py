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
    
    if tupla[0]%2 != 0:
        a = ()
    if tupla[1]%2 != 0:
        b = ()
    if tupla[2]%2 != 0:
        c = ()
    if tupla[3]%2 != 0:
        d = ()
        
        return a+b+c+d