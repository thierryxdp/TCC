"""def uppCons(frase):
    lista = frase.split()
    palavra = ""
    i = 0
    while(i < len(lista)):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            palavra += lista[i].upper()
        else:
            palavra += lista[i]
        i += 1
    return palavra"""
def uppCons(frase):
    lista = list(frase)
    palavra = ""
    i = 0
    while(i < len(lista)):
        if(lista[i] in "bcdfghjklmnpqrstvxwyz"):
            palavra += lista[i].upper()
        else:
            palavra += lista[i]
        i += 1
    return palavra