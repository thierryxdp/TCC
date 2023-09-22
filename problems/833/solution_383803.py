def conta_numero(numero,matriz):
    "retorna o numero de vezes que um inteiro aparec na matriz"
    quantidade = 0
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    return quantidade