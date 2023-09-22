def retira_pontuacao(frase):
    '''Dada uma frase, substitui todos os caracteres de
    pontuação por espaço
    str -> str'''
    frase = str.replace(frase, '.', '')
    frase = str.replace(frase, ',', '')
    frase = str.replace(frase, '!', '')
    frase = str.replace(frase, '?', '')
    frase = str.replace(frase, ':', '')
    frase = str.replace(frase, ';', '')
    frase = str.replace(frase, '-', '')
    return frase

def inverte(frase):
    '''Dada uma frase, retorna uma frase com as mesmas
    palavras na ordem inversa, sem letras maiúsculas e
    sem pontuação
    str -> str'''
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase, ' ')
    list.reverse(frase)
    frase = str.join(' ', frase)
    return frase