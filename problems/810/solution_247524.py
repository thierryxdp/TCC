def retira_pontuacao(frase):
    import string
    p=string.punctuation
    for c in p:
        frase=frase.replace(c," ")
    return frase


def inverte(frase):
    '''Função que dada uma frase retorna uma outra frase porém na ordem inversa; str->str'''
    retira_pontuacao(frase)
    frase = str.split(frase)
    frase.reverse()
    frase = str.join(' ', frase)
    return frase