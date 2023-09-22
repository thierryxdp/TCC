'''Função definida anteriormente'''
def retira_pontuacao(frase):

    frase = frase.replace('.', ' ').replace(',', ' ').replace(':', ' ').replace('?', ' ').replace('?', ' ').replace('-',' ').replace('!',' ')

    return frase
'''Inverte a função separando-a em uma lista e invertendo sua ordem, depois junta a lista em uma string
   str -> str'''
def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.split(frase,' ')
    frase = frase[::-1]
    frase = str.join(' ', frase)
    return frase.lower().replace('  ', ' ')