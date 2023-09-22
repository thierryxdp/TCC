def semPontuação(A):
    pontuação = ".,:?!; "

    for x in pontuação:
        A = A.replace(x, " ")

    return A



def quant_palavras(frase):

    frase = semPontuação(frase)

    h = frase.split()

    return len(h)