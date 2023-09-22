def uppCons(frase):
    '''Funcao que retorna a frase de entrada com todas as sua consoantes em maiusculas'''
    x=0
    vogal=['a','e','i','o','u','A','E','I','O','U']
    while x<len(frase):
        if frase[x] not in vogal:
            frase=str.replace(frase,frase[x],str.upper(frase[x]))
        x=x+1
    return frase