def inverte(frase):
    '''Função que retorna a mesma frase de entrada só que na ordem inversa,
    e sem pontuação.'''
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase, ' ')
    frase = str.join(' ', frase[::-1])
    return frase