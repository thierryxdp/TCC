def myReplace(string, old, new):
    string[0] = string[0].replace(old, new)
    return string

def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    resultado = list(map(
        myReplace,
        len(consoantes)*([frase],),
        consoantes,
        consoantes.upper()
    	))    	
    return resultado[-1][0]