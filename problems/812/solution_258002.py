def retira_pontuacao(frase):
    '''dada uma frase, retorne a frase onde todas as pontuações tenham
sido substituidos por espaço; str -> str'''
    frase1=frase.replace('-', ' ')
    frase2=frase.replace(frase1, '.', ' ')