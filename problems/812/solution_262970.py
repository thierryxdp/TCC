#a função retorna a frase sem pontuação. Estes são substituídos por espaços.
#srt->srt
def retira_pontuacao(frase):
    frase.replace('-',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace('.',' ')
    return(frase)