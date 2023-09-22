def uppCons(frase):
    r=""
    for x in frase:
        if x in ["a","e","i","o","u"]:
            r+=x
        else:
            r+=str.upper(x)
    return r