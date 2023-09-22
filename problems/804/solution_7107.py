def filtra_pares(numero1,numero2,numero3,numero4):
    """A função recebe uma tupla e como parametro, quatro números inteiros, e retorna uma nova tupla, com apenas os numeros pares, na mesma ordem em que se encontrvam"""
    if numero1 % 2 == 0 and numero2 % 2== 0 and numero3 % 2 == 0 and numero4 % 2 ==0:
        return (numero1,numero,2,numero3,numero4)
    if numero2 % 2 == 0: 
        return numero2
    elif numero3 % 2 ==0:
        return numero3
    else:
        return numero4