def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com suas consoantes em maiusculas e o resto sem alteracao
    str->str'''
    i=0
    consoantes=''
    while i<len(frase):
        if 'bcçdfghjklnmpqrstvwxyz' in frase[i] :
            str.join(str.upper(frase[i]),consoantes)
        if 'AEIOUaeiou' in frase[i] :
            str.join(frase[i],consoantes)
        i=i+1
    return consoantes