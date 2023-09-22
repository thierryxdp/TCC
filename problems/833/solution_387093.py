def conta_numero(numero, matriz):
    conta = 0
    n = -1
    while numero < len(matriz):
        if numero in matriz:
            conta = conta + 1
            n = n + 1
        while numero < len(matriz[n]):
           	if numero in matriz[n]:
                conta = conta + 1
return conta