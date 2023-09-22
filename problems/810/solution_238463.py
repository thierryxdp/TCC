import retira_pontuacao
def inverte(frase):
    """ """
    x = str.lower(retira_pontuacao(frase))
    y = str.split(x)
    z = y[::-1]
    return str.join(" ",z)