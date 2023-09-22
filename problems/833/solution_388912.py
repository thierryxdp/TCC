def conta_numero(numero, matriz):
    vezes=0
    
    for linha in matriz:
        for n in linha:
            if numero==n:
                vezes = vezes+1
    return vezes