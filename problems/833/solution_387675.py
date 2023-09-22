def conta_numero(numero,matriz):
    soma=0
    for x in matriz:
        n=x
        soma=soma+list.count(matriz[n],numero)
    return soma