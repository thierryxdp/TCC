def filtra_pares(numeros):
    num1, num2, num3, num4 = numeros
    pares = tuple()

    if num1 % 2 != 0:
        pares = num2, num3, num4
        if num2 % 2 != 0:
            pares = num3, num4
            if num3 % 2 != 0:
                pares = num4
                if num4 % 2 != 0:
                    return 'Não há números pares nessa tupla'
        return pares

    elif num2 % 2 != 0:
        pares = num1, num3, num4
        if num1 % 2 != 0:
            pares = num3, num4
            if num3 % 2 != 0:
                pares = num4
                if num4 % 2 != 0:
                    return 'Não há números pares nessa tupla'
        return pares

    elif num3 % 2 != 0:
        pares = num1, num2, num4
        if num1 % 2 != 0:
            pares = num2, num4
            if num2 % 2 != 0:
                pares = num4
                if num4 % 2 != 0:
                    return 'Não há números pares nessa tupla!'
        return pares

    elif num4 % 2 != 0:
        pares = num1, num2, num3
        if num1 % 2 != 0:
            pares = num2, num3
            if num3 % 2 != 0:
                pares = num2
                if num2 % 2 != 0:
                    return 'Não há números pares nessa tupla!'
        return pares

    else:
        return numeros