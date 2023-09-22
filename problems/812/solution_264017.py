def retira_pontuacao(frase):
    '''Faça uma função que dada uma frase retorne onde toda a pontuação tenham sido substituídas por espaço, str -> str'''
    frase = ''
    if ',' in frase:
        frase = frase.replace(',', ' ')
        return frase