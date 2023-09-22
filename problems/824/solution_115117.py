def uppCons(frase):
    ponto=0
    cons=[]
    while ponto< len(frase):
        if str.lower(frase[ponto]) in "bcdfghjklmnpqrstvxywzç":
            list.append(cons, str.upper(frase[ponto]))
        else:
            list.append(cons,frase[ponto])
        ponto=ponto+1    
    return str.join("", cons)