def conta_numero(numero,matriz):
    '''função que define quantas vezes um número retorna na matriz; dic => int'''
    repete=0
    for linha in matriz:
        repete = repete + list.count(linha,numero)
    return repete