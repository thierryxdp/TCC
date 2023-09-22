def retira_pontuacao(frase):
    remover_pontuacao = ('.', ',', '-', ';', '!', '?', '...')

    for pontuacao in remover_pontuacao:
        frase = frase.replace(pontuacao, ' ')
    return frase

def inverte(frase):
    retira_pontuacao(frase)
    
    frase = frase.split(' ')
    frase = frase[-2::-1]
    return frase