def conta_frases(texto):
    novo_texto = texto.replace('...','.')
    novo_texto = texto.replace('!','.')
    novo_texto = texto.replace('?','.')
    return len(novo_texto.split('.'))-2