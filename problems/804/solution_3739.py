def filtra_pares(numeros):
    '''funçao que dada uma tupla com numeros retorna apenas os pares'''
    numero1 = int(numeros[0])
    numero2 = int(numeros[1])
    numero3 = int(numeros[2])
    numero4 = int(numeros[3])
    def pares(numero1,numero2,numero3,numero4):
        if numero1//2 == 0:
            return True
        else:
            return False
        if numero2//2 == 0:
            return True
        else:
            return False
        if numero3//2 == 0:
            return True
        else:
            return False
        if numero4//2 == 0:
            return True
        else:
            return False
    return filter(pares,numeros)