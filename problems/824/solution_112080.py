def uppCons(frase):
    consoantes='bcdfghjklmnpqrstvxwyz'
    if frase[0] in consoantes:
        return str.replace(frase,frase[0],str.upper(frase[0]))+frase[1:]
    else:
        return frase