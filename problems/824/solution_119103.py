def uppCons (frase):
    ''' essa funçao recebe uma frase e retorna ela com todas as consoantes maiusculas
str -> str'''
    i=0
    vogais= 'aeiouáéíóú'
    while i < len(frase):
        if frase[i] not in vogais:
            frase= frase[:i] +str.upper(frase[i])+frase[i+1:]
        i=i+1
    return frase