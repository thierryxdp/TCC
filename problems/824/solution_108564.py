def uppCons(frase):
    l=0
    s=""
    c="aeiouãíóú"
    while l<len(frase):
        if frase[l] in c:
            s=s+frase[l]
        else:
            s=s+str.upper(frase[l])
        l=l+1
    return s