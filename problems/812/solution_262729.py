def retira_pontuacao(frase):
    a = list(frase)
    p = ("_", "-", ",", ".", "?", "!", ";", ":")
    for n in range(len(p)):
        list.remove(a, p[n])
    return a