def uppCons(frase):
    '''Dado uma frase, retorna a mesma com todas as suas consoantes em maiusculo.str->str'''
    a=0
    c=''
    vogais=['a','e','i','o','u','ú','á','ã','í','é','ó']
    while a<len(frase):
        if frase[a] in vogais:
            c=c+frase[a]
            a=a+1
        if frase[a] not in vogais:
            c=c+frase[a].upper()
            a=a+1
    return c