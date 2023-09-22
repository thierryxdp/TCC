def retira_pontuacao(frase):
    a = list(frase)
    p = ("_", "-", ",", ".", "?", "!", ";", ":")
    for n in range(len(p)):
        if p{n} in a:
            list.remove(a, p[n])
    return a