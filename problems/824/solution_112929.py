def uppCons(frase):
    a=0
    c=''
    vogais=['a','e','i','o','u','ú','á','ã','í','é']
    while a<len(frase):
        if frase[a] in vogais:
            c=c+frase[a]
            a=a+1
        if frase[a] not in vogais:
            c=c+frase[a].upper()
            a=a+1
    return c