def inverte(frase):
    ''' funcao recebe uma frase e retorna ela invertida, apenas com letras 
    minuscula e sem pontuacao'''
    str.upper(frase)
    str.replace(',.:;!?'," ")
    return frase[::-1]