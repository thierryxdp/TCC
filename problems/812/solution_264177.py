pontuacao=[-,:.,;]
def retira_pontuacao(s):
    s.replace(pontuacao," ")
    return s