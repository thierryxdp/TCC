def filtra_pares(x):
    '''Função que recebe uma tupla com quatro elementos inteiros e retorna
    uma nova tupla contendo apenas os elementos pares.
    tuple(int)->tuple(int)'''

    resultado=()

    if x[0]%2==0:
        resultado=resultado+(x[0],)
    if x[1]%2==0:
        resultado=resultado+(x[1],)
    if x[2]%2==0:
        resultado=resultado+(x[2],)
    if x[3]%2==0:
        resultado=resultado+(x[3],)
        
    return resultado