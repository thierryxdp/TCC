def conta_numero(numero, matriz):
    return sum(linha.count(numero) for linha in matriz)