def uppCons(frase):
    i=0
    vogais=['a','e','i','o','u','A','E','I','O','U']
    l=list(frase)
    while i<len(l):
        if frase[i] in vogais:
            i=i+1
        else:
            l[i]=str.upper(l[i])
            i=i+1
    return str.join(l,'')