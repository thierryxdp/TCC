pontuacao=[-,:.,;]
def retira_pontuacao(s):
    x=s.split("-;.,:")
    a=" ".join(x)
    return a