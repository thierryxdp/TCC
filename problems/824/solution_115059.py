def uppCons(frase):
    ponto=0
    while ponto<len(frase):
        if not frase[ponto]=='a' or frase[ponto]=='e' and frase[ponto]=='i' and frase[ponto]=='o' and frase[ponto]=='u':
            frase[ponto]= frase[ponto].upper
        ponto=ponto+1
    return frase