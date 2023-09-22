def conta_numero(numero,matriz):
    soma=0
    for i in matriz:
        if i in matriz:
            soma=soma+list.count(i,numero)
    return soma