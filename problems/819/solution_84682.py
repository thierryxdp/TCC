def filtraMultiplos(lista,n):
    '''funçao que recebe uma lista de numeros e um numero
    e retorna uma nova lista com os elementos da original que
    são divisiveis por este numero'''
    i=0
    lista=[]
    while lista%n==0:
        i=i+1
    return lista