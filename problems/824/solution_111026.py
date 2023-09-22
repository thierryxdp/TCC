def uppCons(frase):
    """função que dada uma frase, a retorne com suas consoantes em maiusculo;str-->str"""
    NovaFrase=' '
    i=0
    while i<len(frase):
        consoante=frase[i]
        if consoante in 'bcdfghjklmnpqrstvwxyz':
            consoante= str.upper(consoante)
            NovaFrase+=consoante
            i+=1
            return NovaFrase