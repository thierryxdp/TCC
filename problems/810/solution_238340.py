def inverte(frase):
    remover_pontuacao = ('.', ',', '-', ';', '!', '?', '...')

    for pontuacao in remover_pontuacao:
        frase = frase.replace(pontuacao, ' ')
    frase = frase.split(' ')
    frase = frase[-2::-1]
    frase = ' '.join(frase)
    return lower(frase)