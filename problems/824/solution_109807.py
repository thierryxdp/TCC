def myReplace(string, old, new):
    string[0] = string[0].replace(old, new)
    print(string)
    return None

def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    map(myReplace, len(consoantes)*[[frase]], consoantes, consoantes.upper())
    return frase