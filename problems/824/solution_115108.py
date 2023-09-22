def uppCons(frase):
    ponto=0
    cons=[]
    while len(frase)>ponto:
        if str.lower(frase[ponto])not in "aeiou":
            cons=cons+str.upper(frase[ponto])
        else:
            cons=cons+str.lower(frase[ponto])
        i=i+1
    return str.join("",frase2)