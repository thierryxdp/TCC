def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    x=frase.replace(',', ' ')
    x=frase.replace('.', ' ')
    x=frase.replace(';', ' ')
    x=frase.replace(':', ' ')
    x=frase.replace('!', ' ')
    x=frase.replace('?', ' ')
    x=frase.replace('-', ' ')
    return x