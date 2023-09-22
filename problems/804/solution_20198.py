def filtra_pares(x):
    '''Função que receba uma tupla com quatro elementos inteiros como parâmetro, e retorne uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam; tupla -> tupla'''
    pares=[]
    if x[0]%2==0:
        pares.insert(0,x[0])
    if x[1]%2==0:
        pares.insert(1,x[1])
    if x[2]%2==0:
        pares.insert(2,x[2])
    if x[3]%2==0:
        pares.insert(3,x[3])
    return tuple(pares)