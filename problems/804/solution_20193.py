def par(num):
    '''Retorna true se um numero é par ou false se ímpar'''
    return num%2==0

def filtra_pares(lista):
    '''Filtra todos os numeros pares da lista de entrada, list -> list'''
    resultado = ()
    
    if par(lista[0]):
        resultado += lista[0:1]
    if par(lista[1]):
        resultado += lista[1:2]
    if par(lista[2]):
        resultado += lista[2:3]
    if par(lista[3]):
        resultado += lista[3:]
    return resultado