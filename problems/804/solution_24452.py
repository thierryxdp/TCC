#Start your python function here
def filtra_pares(tupla):
    '''recebe uma tupla de 4 elementos do tipo inteiro
    e retorna uma nova tupa contendo apenas os elementos pares
    na mesma ordem em que se encontravam
    tuple (int,int,int,int) -> tuple'''
    pares = []
    for num in tupla:
        pares.insert(len(tupla),num) if (num%2)==0 else False
    return tuple(lista)