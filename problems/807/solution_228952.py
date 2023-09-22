'''Funcao que recebe um texto e retorna o numero de frases que existem no texto, separadas
    pelos caracteres '.','!','?','...'.
    str -> int
    '''
def conta_frases(texto):
    join_texto = str.join('', str.split(texto,' '))
    f1 = str.join(' ', str.split(join_texto, '.'))
    f2 = str.join(' ', str.split(f1, '!'))
    f3 = str.join(' ', str.split(f2, '?'))
    return len(f3.split())