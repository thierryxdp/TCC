def pontuacao():
    return list(',','.','?','!)
            
def retira_pontuacao(frase):
    return str.replace(pontuacao, '')