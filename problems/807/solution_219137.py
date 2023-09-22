def conta_frases(texto):
    pontuacao = ['.','!','?','...']
    texto = str.count(texto, 'pontuacao')
    return texto