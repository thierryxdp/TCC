'''Substitui a pontuação por espaços
   str->str'''
def retira_pontuacao(frase):

    frase = frase.replace('.', ' ').replace(',', ' ').replace(':', ' ').replace('?', ' ').replace('?', ' ').replace('-',' ').replace('!',' ')
    
    return frase