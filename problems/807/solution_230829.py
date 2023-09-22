def conta_frases(texto):
    '''Dado um texto, a função retorna o número de 
    fases que aparecem nesse texto, considerando que
    uma frase termina quando os caractéres !, ?, ., ...,
    aparecem no texto. str -> int'''
    n=texto.split('.'))
    n=texto.split('!'))
    n=texto.split('?'))
    n=texto.split('...'))
    return len(n)