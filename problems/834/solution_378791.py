def media_matriz(matriz):
    soma_total = 0
    qnt_num = 0
    for linha in matriz:
        soma_total += sum(linha)
        qnt_num += len(linha)
    return round(soma_total/qnt_num, 2)