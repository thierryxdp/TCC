def retira_pontuacao(frase):
    remover_pontuacao = ('.', ',', '-', ';', '!', '?', '...')

    for pontuacao in remover_pontuacao:
        frase = frase.replace(pontuacao, ' ')
    return frase