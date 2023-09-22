def conta_numero(numero,matriz):
    '''Esta função retorna quantas vezes um número n é encontrado em uma matriz m.
int, list(list) --> int
'''
    cont = 0
    for linha in matriz:
        for col in linha:
            if numero == col:
                cont += 1
    return cont