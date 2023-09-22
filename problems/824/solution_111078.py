def uppCons(frase):
    """função que dada uma frase de entrada, retorne a frase com suas consoantes em maiúsculo;string-->string"""
    NovaFrase=''
    i=0
    while i<len(frase):
        consoante=frase[i]
        if consoante in 'bcdfghjklmnpqrtvwxyzç':
            consoante=str.upper(consoante)
        NovaFrase+=consoante
        i+=1
    return NovaFrase