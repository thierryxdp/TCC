def retira_pontuacao(x):
    str.replace(x, "...", " ")
    for i in x:
        if i in "./,:;!1-?":
            x = str.replace(x, i, " ")
    return x