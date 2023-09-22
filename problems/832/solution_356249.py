def eh_quadrada(matriz):
    """ função que dado uma matrix identifica de essa é quadrada ou não;
    list -> booleana """
    if len(matriz) == len(matriz[0]):
        return 'True'
    elif len(matriz) == 0:
        return 'True'
    else:
        return 'False'