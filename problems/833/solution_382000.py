def conta_numero(numero,matriz):
    soma = 0
    while numero in matriz:
        soma = soma + 1
    numero = numero + 1
    return soma