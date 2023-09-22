def conta_numero(numero, matriz):
    soma = 0
    for i in (range(len(matriz))):
        if numero in matriz[i]:
            soma = soma + matriz[i].count(numero)
        else:
            pass
    return soma