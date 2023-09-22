def eh_quadrada(matriz):
    qnt_i = 0
    qnt_j = 0
    for i in matriz:
        qnt_i += 1
    for j in matriz[0]:
        qnt_j += 1
    return qnt_i == qnt_j