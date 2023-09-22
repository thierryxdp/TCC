def conta_frases(texto):
    pontuacao1 = texto.count('.')
    pontuacao2 = texto.count('!')
    pontuacao3 = texto.count('?')
    pontuacao4 = texto.count('...')-2
    return pontuacao1+pontuacao2+pontuacao3+pontuacao4