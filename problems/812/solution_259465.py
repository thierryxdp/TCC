def retira_pontuacao(frase):
    ''''Retorna a frase inserida com espaços no lugar dos sinais de pontuação
str -> str'''
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    return frase