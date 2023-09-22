#a funcao substitui todos os pontos da frase por espaco
def retira_pontuacao(x):
    if ',' in (x):
        return str.replace(',' ' ',)