def retira_pontuacao(A):
    pontuacao = "- , : ? ! . ; "

    for x in pontuacao:
        A = A.replace(x, " ")

    return A

def inverte(I):
    I = I.lower()
    I = retira_pontuacao(I)
    K = I.split()
    return (" ".join((K[::-1])))