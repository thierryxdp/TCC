def myReplace(string, old, new):
    string[0] = string[0].replace(old, new)
    return string
    # return None

def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    resultado = next(map(myReplace, len(consoantes)*[[frase]], consoantes, consoantes.upper()))
    return resultado