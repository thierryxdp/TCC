#Start your python function here
def filtra_pares(numeros):
    lista=[numeros]
    filter(lambda x:numeros%2==0,lista)
    return lista