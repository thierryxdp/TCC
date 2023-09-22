def retira_pontuacao(frase):
    n1 = 0
    n1 += str.strip(frase, "-")
    n1 += str.strip(frase, ",")
    n1 += str.strip(frase, ":")
    n1 += str.strip(frase, ";")
    n1 += str.strip(frase, ".")
    n1 += str.strip(frase, "!")
    n1 += str.strip(frase, "?")

    return n1