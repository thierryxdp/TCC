def retira_pontuacao(frase):
    import string
    p=string.punctuation
    for c in p:
        frase=frase.replace(c," ")
    return frase


def inverte(frase):
    '''Função que dada uma frase retorna uma outra frase porém na ordem inversa; str->str'''
    fra=retira_pontuacao(frase)
    fra = str.split(fra)
    fra.reverse()
    fra = str.join(' ', fra)
    return str.lower(fra)