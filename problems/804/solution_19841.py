def filtra_pares(numeros):
    '''função que retorna os elementos da entrada que são pares,dado os números n1,n2,n3 e n4;tupl(int,int,int,int)->tupla'''
    pares=()
    if numeros[0]%2==0:
        pares+=tuple(numeros[0:1])
    if numeros[1]%2==0:
        pares+=tuple(numeros[1:2])
    if numeros[2]%2==0:
        pares+=tuple(numeros[2:3])
    if numeros[3]%2==0:
        pares+=tuple(numeros[-1:2:-1])
    return pares