def uppCons(frase):
    ponto=0
    cons=[]
    while ponto< len(frase):
        if str.lower(frase[ponto]) in "bcdfghjklmnpqrstvxywzç":
            cons= cons + str.upper(frase[ponto]))
        else:
            cons= cons + frase[ponto]
        ponto=ponto+1    
    return str.join("", cons)