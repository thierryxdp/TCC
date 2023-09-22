def uppCons(frase):
    indice=0
    frase_nova = ''
    consoantes = 'bcdfghjklmnpqrstvxz'
    while indice<len(frase):
        if frase[indice] == consoantes:
            uppconsoante = str.upper(consoantes)
            return uppconsoante
            frase_nova=frase_nova + uppconsoante
        else:
            frase_nova+=frase[indice]
        indice = indice+1
    return frase_nova