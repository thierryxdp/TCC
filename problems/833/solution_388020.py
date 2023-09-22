def conta_numero(numero,matriz):
    ocorrencias = []
    for numero in matriz:
        n = list.count(matriz,numero)
        list.append(ocorrencias,n)
    return ocorrencias