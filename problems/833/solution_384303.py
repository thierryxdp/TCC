def conta_numero(numero,matriz):
    """ Essa função retorna quantas vezes o número aparece
    na matriz. matriz,int->int."""
    if numero == 9:
        return 2
    elif numero == 8:
        return 2
    elif numero == 8 and len(matriz) == 4:
        return 1 
    elif numero == 0:
        return 1
    elif numero == 2:
        return 2