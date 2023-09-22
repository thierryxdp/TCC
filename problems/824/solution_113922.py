def uppCons(frase):
    """recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas e as vogais da mesma forma como estavam"""
    contador = 0
    frasetolist = [frase]
    while contador<len(frasetolist):
        if frasetolist[contador] in "bcdfghjklmnpqrstvxwyz":
            frasetolist[contador] = str.upper(frasetolist[contador])
            contador +=1
        else:
            contador +=1
    return str(frasetolist)