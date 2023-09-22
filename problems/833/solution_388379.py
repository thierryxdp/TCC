def conta_numero(numero, matriz):
    counter = 0
    
    for linha in matriz:
        counter = counter + linha.count(numero)
    return counter