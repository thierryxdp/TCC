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
    '''função que inverte as palavras de uma dada lista 
    list -> list'''
    retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = frase.split(' ')
    list.reverse(frase)
    frase = ' '.join(frase)
    return frase