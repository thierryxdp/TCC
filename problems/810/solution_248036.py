def retira_pontuacao(frase):
    '''função que retira toda a pontuação de uma frase sem exceção
    string -> string'''
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace(',', ' ')
    return frase

def inverte(frase):
    '''função que inverte as palavras de uma dada frase
    str -> str'''
    retira_pontuacao(frase)
    x = str.lower(frase)
    x = x.split(' ')
    list.reverse(x)
    x = ' '.join(x)
    return x