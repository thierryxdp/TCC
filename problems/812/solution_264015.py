def retira_pontuacao(frase):
    '''Faça uma função que dada uma frase retorne onde toda a pontuação tenham sido substituídas por espaço, str -> str'''
    return frase.replace(',', ' ') not frase.replace('.', ' ') not frase.replace('?', ' ') and frase.replace('!', ' ')