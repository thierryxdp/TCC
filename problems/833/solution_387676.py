def conta_numero(numero,matriz):
    soma=0
    for n in matriz:
        soma=soma+list.count(n,numero)
    return soma