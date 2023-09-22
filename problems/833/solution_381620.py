def conta_numero(numero, matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += 1
            if numero in len(total):
                ocorrencia = list.count(total, numero)
                return ocorrencia