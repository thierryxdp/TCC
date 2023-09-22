simbolos_pontuacao: (',','!','.','?',';')

def retira_pontuacao(frase):
    for c in simbolos_pontuacao:
        frase = frase.replace(c, '')