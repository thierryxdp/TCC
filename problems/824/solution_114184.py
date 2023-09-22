def uppCons(frase):
    """função que retorna uma frase com as consoantes em maiúsculo
    str=>str"""
    lista = list(frase)
    palavra = ""
    i = 0
    while(i < len(lista)):
        if(lista[i] in "bçcdfghjklmnpqrstvxwyz"):
            palavra += lista[i].upper()
        else:
            palavra += lista[i]
        i += 1
    return palavra