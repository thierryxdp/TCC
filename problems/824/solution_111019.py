def uppCons(frase):
    """função que dada uma frase, a retorne com suas consoantes em maiusculo;str-->str"""
    frase=list(frase)
    i=0
    frase=()
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase= frase+1
            i=i+1
            return (frase[1].upper).join