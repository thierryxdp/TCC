def uppCons(frase):
    i=0
    lista=[]
    while i<len(frase):
        if frase[i] in "qwrtypsdfghjklçzxcvbnm":
            novo=str.upper(frase[i])
            a=list(frase)
        i=i+1
    return a