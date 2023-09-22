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

#Questão 5
def inverte(frase):
    '''Retorna a frase inserida com as palavras na ordem inversa, sem letras maiúsculas e sem pontuação
str -> str'''
    frase=str.lower(frase)
    frase=retira_pontuacao(frase)
    frase=str.split(frase)
    return str.join(' ',(frase[::-1]))