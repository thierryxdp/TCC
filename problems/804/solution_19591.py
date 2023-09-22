def filtra_pares(valores):
    '''funçao que recebe uma tupla com quatro elementos inteiros como parametro, e retorna
    uma nova tupla contendo apenas os elementos pares.
    tuple -> tuple'''
    filtro=[]
    for x in valores:
        if x%2==0:
            filtro +=[x]
    return tuple(filtro)