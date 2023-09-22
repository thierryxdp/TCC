def conta_numero(numero,matriz):
    soma=0
    for num in matriz:
        soma=soma+list.count(matriz[num],numero)
    return soma