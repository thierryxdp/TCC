def conta_numero(numero,matriz):
    """Função que dada uma matrz de inteiros, conta e retrorne quantas vezes aquele
    n° aparece na matriz; int,list=>list"""
    x = 0
    for linha in matriz:
        x = x + list.count(linha,numero)
    return x