def filtra_pares(t):
    '''Função que recebe uma tupla contendo quatro numeros inteiros e retorna outra apenas com os numeros pares. 
    tuple -> tuple'''
    f=()
    if t[0]%2==0:
        f= f + (t[0],)
    if t[1]%2==0:
        f= f + (t[1],)
    if t[2]%2==0:
        f= f + (t[2],)    
    if t[3]%2==0:
        f= f + (t[3],)   
    return f