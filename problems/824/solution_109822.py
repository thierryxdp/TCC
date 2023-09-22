def myReplace(string, old, new):
    string[0] = string[0].replace(old, new)
    return string[0]

def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    resultado = list(map(
        myReplace,
        len(consoantes)*([frase],),
        consoantes,
        consoantes.upper()
    	))    	
    return resultado[-1]