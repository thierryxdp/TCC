def conta_numero(numero,matriz):

    resposta = 0

    for matrizes in matriz:

        if numero in matrizes:

            resposta = resposta + matrizes.count(numero)

    return resposta