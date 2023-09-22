def inverte(frase):
    remover_pontuacao = ('.', '-', ';', '!', '?', '...')
    
    frase = frase.replace(',', '')
    for pontuacao in remover_pontuacao:
        frase = frase.replace(pontuacao, ' ')
    frase = frase.split(' ')
    frase = frase[-2::-1]
    frase = ' '.join(frase)
    return str.lower(frase)