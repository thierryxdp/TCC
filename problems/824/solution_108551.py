def uppCons(frase):
    l=0
    c="aeiou"
    while l<len(frase):
        if frase[l] in c:
            str.upper(frase,frase[l])
        l=l+1
    return frase