def busca(string, matriz):

    resposta = []

    for matrizes in matriz:

        if matrizes[2] == string:

            matrizes.remove(string)

            resposta.append(matrizes)

    resposta.remove(string)

    return resposta