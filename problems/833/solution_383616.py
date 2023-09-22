def conta_numeros(numero,matriz):

    contador=0
    for linha in matriz:
        for n in linha:
            if n==numero:
                contador+=1
    return contador