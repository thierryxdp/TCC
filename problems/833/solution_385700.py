def conta_numero(numero, matriz):
    qnt_num = 0
    for lista in matriz:
        qnt_num += lista.count(numero)
    return qnt_num