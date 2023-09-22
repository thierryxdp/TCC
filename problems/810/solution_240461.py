def inverte(frase):
    '''Retorna a frase inserida com as palavras na ordem inversa, sem letras maiúsculas e sem pontuação
str -> str'''
    frase=str.lower(frase)
    frase=retira_pontuacao(frase)
    frase=str.split(frase)
    return str.join(' ',(frase[::-1]))