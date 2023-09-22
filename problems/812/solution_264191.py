pontuacao=[-,:.,;]
def retira_pontuacao(s):
    x=s.split("-;.,:")
    a=x.join(" ",x)
    return a