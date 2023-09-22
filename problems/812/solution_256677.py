def retira_pontuacao(frase):
    '''substitui os caracteres de pontuação de uma frase por espaços'''
    return frase.replace('—',' '), frase.replace(',',' '), frase.replace(':', ' '), frase.replace(';', ' '), frase.replace([-1], ' ')