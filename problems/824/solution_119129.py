def uppCons(frase):
    i=0
    vogais=['a','e','i','o','u','A','E','I','O','U']
    list(frase)
    while i<len(frase):
        if frase[i] in vogais:
            i=i+1
        else:
            frase[i]=str.upper(frase[i])
            i=i+1
    return list.join(frase,'')