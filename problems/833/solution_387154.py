def conta_numero(numero, matriz):
    a = [item for sublist in matriz for item in sublist]
    return a.count(numero)