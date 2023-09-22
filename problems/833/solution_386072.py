def conta_numero(numero,matriz):
    i = 0
    soma = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            lista = matriz[i]
            if lista[j] == numero:
                soma = soma + 1
            j = j + 1
        i = i + 1
    return soma