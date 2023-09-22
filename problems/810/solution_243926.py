def inverte(frase):
    ''' funcao recebe uma frase e retorna ela invertida, apenas com letras 
    minuscula e sem pontuacao'''
    str.upper(frase)
    pontuacao = "-,:;.,?!"
    for p in pontuacao:
        frase = str.replace(p," ")
        return frase[::-1]