def retira_pontuacao(frase):
    '''Faça uma função que dada uma frase retorne onde toda a pontuação tenham sido substituídas por espaço, str -> str'''
    if frase.replace(',', ' '):
        return frase
    elif frase.replace('.', ' '):
        return frase