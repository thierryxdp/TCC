def conta_numero(numero,matriz):
    """Funcao que conta quantas vezes o numero aparece na matriz;
    Entrada: int, list
    Saida: int"""
    qt=0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                qt+=1
    return qt