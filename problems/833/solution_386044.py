def conta_numero(numero,matriz):
    total = 0
    for i in matriz:
        for j in i:
            if numero == j:
                total = total + 1
                return total