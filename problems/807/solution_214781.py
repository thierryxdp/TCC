def conta_frases(frases):
    """Dada um texto armazenado em uma string cria uma função que conta o número de frases que aparecem nesse texto.
    Cada frase é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos em sequência(reticências.
    return str.count(frases, '.') + str.count(frases, '?') + str.count(frases, '!') - 2*str.count(frases, '...')