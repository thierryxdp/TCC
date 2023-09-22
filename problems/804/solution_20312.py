def filtra_pares(x):
    '''Função que receba uma tupla com quatro elementos inteiros como parâmetro e devolve uma tupla contendo os valores pares da tupla original, na mesma ordem; tupla -> tupla'''
    pares = ()
    
    if x [0]%2==0:
        pares = pares + (x[0],)
    if x [1]%2==0:
        pares = pares + (x[1],)
    if x [2]%2==0:
        pares = pares + (x[2],)
    if x [3]%2==0:
        pares = pares + (x[3],)
    if x[4]%2==0:
        pares = pares + (x[4],)
        return pares