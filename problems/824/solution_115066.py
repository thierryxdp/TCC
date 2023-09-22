def uppCons(frase):
    ponto=0
    vogais= 'a,e,i,o,u'
    while ponto<len(frase):
        if frase[ponto]not in vogais:
            frase[ponto]= [frase[ponto].upper]
        ponto=ponto+1
    return frase