def conta_frases(texto):
    '''Dado um texto, a função retorna o número de 
    fases que aparecem nesse texto, considerando que
    uma frase termina quando os caractéres !, ?, ., ...,
    aparecem no texto. str -> int'''
    n=0
    n=n+(len(texto.split('.')))
    n=n+(len(texto.split('!')))
    n=n+(len(texto.split('?')))
    n=n+(len(texto.split('...')))
    return n