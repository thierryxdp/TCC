def retira_pontuacao(frase):
    ''' Essa função tem objetivo tirar todas os caracteres de ontuação de dado uma frase, str, str,str'''
    frase1 = str.join(" ", str.split(frase)'.')
    frase2 = str.join(" ", str.split(frase1)',')
    frase3 = str.join(" ", str.split(frase2)'!')
    frase4 = str.join(" ", str.split(frase3)'?')
    frase5 = str.join(" ", str.split(frase4)'-')
    return frase5