def conta_numero(numero,matriz):
    '''Retorna quantas vezes o numero fornecido aparece
    na matriz de entrada
    int,list -> int'''
    rep = 0
    for linha in matriz:
        for elemento in linha:
            if numero == elemento:
                rep = rep + 1
    return rep