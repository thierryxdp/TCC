def conta_numero(numero,matriz):
    contagem=0
    for linha in matriz:
        for num in linha:
            if num==numero:
                contagem=contagem+1
    return contagem