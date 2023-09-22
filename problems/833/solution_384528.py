def conta_numero(numero,matriz):
    """conta quantas vezes certo número dado é encontrado em certa matriz dada. INT,LIST->INT"""
    contagem=0
    for linha in matriz:
        for num in linha:
            if num==numero:
                contagem=contagem+1
    return contagem