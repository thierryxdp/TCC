def filtra_pares (numeros):
    """Função que recebe uma tupla com quatro elementos inteiros como parâmetro, e retorna uma 
    nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.
    tuple -> tuple"""
    num1, num2, num3, num4 = numeros
    pares = ()
    impares = ()
    if num1 % 2 == 0:
        pares = pares + (num1)
    else:
        impares = impares + (num1,)
    if num2 % 2 == 0:
        pares = pares + (num2,)
    else:
        impares = impares + (num2,)
    if num3 % 2 == 0:
        pares = pares + (num3,)
    else:
        impares = impares + (num3,)
    if num4 % 2 == 0:
        pares = pares + (num4,)
    else:
        impares = impares + (num4,)             
    return pares#Start your python function here