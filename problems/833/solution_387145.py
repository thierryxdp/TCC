def conta_numero(numero,matriz):
    """Dado um númeor inteiro e uma matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele número aparece na matriz"""
    quantas_vezes = 0
    for linha in matriz:
        for n in linha:
            if n == numero:
                quantas_vezes += 1
    return quantas_vezes