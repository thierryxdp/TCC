def uppCons(frase):
    '''funcao que recebe uma frase como entrada e retorna a mesma frase com todas as consoantes em maiusculas
    str -> str'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase=str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase