def conta_numero(numero,matriz):
    """Conta quantas vezes o elemento numero aparece na matriz dada. int,list --> int"""
    quantidade = 0
    for linha in matriz:
        quantidade += list.count(linha,numero)
    return quantidade