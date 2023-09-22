def uppCons(frase):
    '''retorna a frase com todas as consoantes em maiusculo;
    entrada-> frase; str->str'''
    x=0
  	while x < len(frase):
        if 'bcdfghjklmnpqrstvwyz' in frase[x]:
            str.upper(frase[x])
        x=x+1
    return frase