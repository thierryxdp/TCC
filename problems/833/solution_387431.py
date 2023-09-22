def conta_numero(numero, matriz):
    contador = 0
    for i in matriz:
        if numero == matriz[i]:
            contador += 1
    return contador