def retira_pontuacao(A):
    pontuacao = "- , : ? ! . ; "

    for x in pontuacao:
        A = A.replace(x, " ")

    return A