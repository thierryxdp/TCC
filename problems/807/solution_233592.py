def semPontuacao(A):
    pontuacao = ".,:?!; "

    for x in pontuacao:
        A = A.replace(x, " ")

    return A


def juntaPalavras(B):
    espacos = " "
    
    for z in espacos:
        B = B.replace(z,"")

        return B


def conta_frases(C):
    C = juntaPalavras(C)
    C = semPontuacao(C)

    J = C.split()

    return len(J)