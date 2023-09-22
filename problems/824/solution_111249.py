def uppCons(frase):
    '''dada ua frase, transforma em caixa alta suas consoantes
    srt->str'''
    frase=list(frase)
    i=0
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvxwyzç":
            frase[i]= frase[i].upper()
        i=i+1
    return ''.join(frase)