def retira_pontuacao(frase):
    a = list(frase)
    p = ("_", ",", ".", "?", "!", ";", ":", "-")
    for n in 3*range(len(p)):
        if p[n] in a:
            list.remove(a, p[n])
    return "".join(a)