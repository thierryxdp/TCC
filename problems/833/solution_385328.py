def conta_numero(nurmero,matriz):
    """retorna quantas vezes o numero aparece na matriz.
    int,list->int"""
    contagem=0
    for linha in matriz:
        for valor in linha:
            if valor==numero:
                contagem=contagem+1
    return contagem