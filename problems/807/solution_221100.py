def conta_frases(texto):
    """Função que calcula a quantidade de frases que possui um texto. Na entrada ela recebe um string
    e devolve na saída a quantidade de frases."""
    pontuacao1 = texto.count('.')
    pontuacao2 = texto.count('!')
    pontuacao3 = texto.count('?')
    pontuacao4 = texto.count('...')
    return pontuacao1+pontuacao2+pontuacao3+pontuacao4 - (3*pontuacao4)