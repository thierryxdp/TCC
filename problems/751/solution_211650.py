def semPontuacao(A):
    pontuacao = ".,:?!; "

    for x in pontuacao:
        A = A.replace(x, " ")

    return A



def quant_palavras(frase):

    frase = semPontuacao(frase)

    h = frase.split()

    return len(h)