def filtra_pares([num1,num2,num3,num4]):
    '''
    dado 4 numeros inteiros, a função 
    retorna apenas os numeros pares,
    seguindo a ordem em que foram escolhidos.
    '''
    if num1%2 == 0:
        if num2%2 == 0:
            if num3%2 == 0:
                if num4%2 == 0:
                    return num1, num2, num3, num4