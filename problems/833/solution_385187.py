def conta_numero(numero,matriz):
    'funcao que encontra o numero de vezes que um numero aparece em uma matriz'
    contador=0
    for linha in matriz:
        for elementos in linha:
            if numero == elementos:
                contador+=1
    return contador