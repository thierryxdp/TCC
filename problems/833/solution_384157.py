def conta_numero(numero,matriz):

    contador=0
    for linha in matriz:
        for elem in linha:
            if numero == elem:
                contador+=1

    return contador