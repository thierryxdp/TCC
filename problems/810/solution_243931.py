def inverte(frase):
    ''' funcao recebe uma frase e retorna ela invertida, apenas com letras 
    minuscula e sem pontuacao'''
    str.upper(frase)
    str.replace(frase,',.:;!?'," ")
    return frase[::-1]