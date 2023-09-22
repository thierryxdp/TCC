def myReplace(string, old, new):
    string[0] = string[0].replace(old, new)
    return string

def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    resultado = [frase]
    map(
        myReplace,
        len(consoantes)*[resultado],
        consoantes,
        consoantes.upper()
    	)    	
    return resultado[0]