def semPontuação(A):
    pontuação = ".,:?!; "

    for x in pontuação:
        A = A.replace(x, " ")

    return A


def juntaPalavras(B):
    espacos = " "
    
    for z in espacos:
        B = B.replace(z,"")

        return B


def conta_frases(C):
    C = juntaPalavras(C)
    C = semPontuação(C)

    J = C.split()

    return len(J)