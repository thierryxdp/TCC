def filtra_pares(x):
    """Função que recebe quatro elementos inteiros e retorna uma tupla somente com os números pares"""
    par=[]
    
    if x[0]%2==0:
        par=par+[x[0]]
    
    if x[1]%2==0:
        par=par+x[1]
    
    if x[2]%2==0:
        par=par+x[2]
    
    if x[3]%2==0:
        par=par+x[3]
    
    return par