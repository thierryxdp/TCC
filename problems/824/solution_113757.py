def uppCons (frase):
    x=frase.upper()
    p=0
    teste=""
    while p<len(frase):
        if x[p]=='AEIOUaeiou':
            teste=teste+frase[p].lower()
        p=p+1
    return teste