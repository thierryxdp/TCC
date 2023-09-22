def uppCons(frase):
    '''retorna a frase com todas as consoantes em maiusculo;
    entrada-> frase; str->str'''
    x=0
  	while x<len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwyz':
            str.upper(frase[x])
        x=x+1
    return frase