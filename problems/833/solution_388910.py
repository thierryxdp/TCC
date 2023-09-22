# Questão 2
def conta_numero(numero, matriz):
    q = 0
    for linha in matriz:
        for j in linha:
            if numero == j:
                q +=1
    return q