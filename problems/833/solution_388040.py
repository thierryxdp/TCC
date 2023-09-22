def conta(numero,matriz):
    ocorrencias = 0
    for numero in matriz:
        qnt = list.count(matriz,numero)
        list.append(ocorrencias,qnt)
    return ocorrencias