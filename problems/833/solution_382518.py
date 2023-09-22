def conta_numero(numero,matriz):
    '''Retorna quantas vezes o numero ocorre na matriz
    int,lista->int'''
    qtd=0
    for linha in matriz:
        qtd+=linha.count(numero)
    return qtd