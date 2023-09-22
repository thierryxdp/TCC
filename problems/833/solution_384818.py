def conta_numero(n, matriz):
    total = 0
    for linha in matriz:
        for elemento in linha: 
            if elemento == n:
                total = total + 1
    return total