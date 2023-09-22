def conta_frases(texto):
    """Dado um texto, retorna o número de frases que aparecem nesse texto"""
    contador = str.count(texto, '...')
    frase = texto.replace('...',' ')
    contador = contador + str.count(frase,'!')
    frase = frase.replace('!', ' ')
    contador = contador + str.count(frase,'?')
    frase = frase.replace('?', ' ')
    contador = contador + str.count(frase,'.')
    frase = frase.replace('.', ' ')
    return contador