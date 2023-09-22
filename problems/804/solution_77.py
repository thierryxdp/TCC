def filtra_pares(inteiros):
    '''recebe uma tupla com 4 elementos inteiros, e retorna uma tupla com aqueles que forem pares
    tupla-->tupla'''
    if(int(inteiros[0])%2==0):
        pares=inteiros[0]
    if(int(inteiros[1])%2==0):
        pares+=inteiros[1]
    if(int(inteiros[2])%2==0):
        pares+=inteiros[2]
    if(int(inteiros[3])%2==0):
        pares+=inteiros[3]
        
    return pares