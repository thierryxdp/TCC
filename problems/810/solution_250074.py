def inversa(x=""):
    x=retira_pontuacao(x)
    x=x.split(" ")
    return str(" ").join(x[::-1])