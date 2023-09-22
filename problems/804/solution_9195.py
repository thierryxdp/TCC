#Start your python function here
def filtra_pares(numeros):
    '''
    Função que recebe uma tuple com quatro números inteiros e retorna uma nova tuple contendo apenas os elementos pares da tuple originl, na mesma ordem
    tuple -> tuple
    '''
    n1 = numeros[0]
    n2 = numeros[1]
    n3 = numeros[2]
    n4 = numeros[3]
    par = ()
    if (n1%2==0):
        par = par + (n1,)
    if (n2%2==0):
        par = par + (n2,)
    if (n3%2==0):
        par = par + (n3,)
    if (n4%2==0):
        par = par + (n4,)
    return par