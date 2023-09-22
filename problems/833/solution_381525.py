def conta_numero(numero,matriz):
    """Retorna a quantidade de vezes que um numero aparece na matriz. int,list-->int"""
    vezes=0
    for linha in matriz:
        for coluna in linha:
            if coluna==numero:
                vezes=vezes+1
    return vezes