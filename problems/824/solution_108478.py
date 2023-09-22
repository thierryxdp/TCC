def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in "qwrtypsdfghjklçzxcvbnm":
            novo=str.upper(frase[i])
            del frase[i]
            list.insert(frase,i,novo)
        i=i+1
    return frase