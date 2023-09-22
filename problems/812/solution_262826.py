def retira_pontuacao(frase):
    '''Essa função recebe uma frase e retira suas pontuações
    str -> str'''
    lista = str.split(frase, '.')
    frase = str.join(' ', lista)
    lista = str.split(frase, '?')
    frase = str.join(' ', lista)
    lista = str.split(frase, '!')
    frase = str.join(' ', lista)
    lista = str.split(frase, '-')
    frase = str.join(' ', lista)
    lista = str.split(frase, ',')
    frase = str.join(' ', lista)
    lista = str.split(frase, ':')
    frase = str.join(' ', lista)
    lista = str.split(frase, ';')
    frase = str.join(' ', lista)
    return frase