def pontuacao():
    return (',','.','?','!)
            
def retira_pontuacao(frase):
    return str.replace(pontuacao, '')