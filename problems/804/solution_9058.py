#Questão 6
def par(n):
    '''Retorna se um número é par
int -> bool'''
    if n%2==0:
        return True
    else:
        return False
def filtra_pares(tup):
    '''Recebe uma tupla com quatro elementos inteiros e retorna uma tupla contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam.
tuple -> tuple'''
    return list(filter(par, tup))