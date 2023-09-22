def uppCons(frase):
    """Retorne uma frase com todas consoantes maiusculas;
    str -> str"""
    cont = 0
    consoantes = "bcdfghjklmnpqrstvwxyz"
    frase_nova = ""
    while cont < len(frase):
        if frase[cont] in consoantes:
            frase_nova += frase[cont].Upper()
        else:
            frase_nova += frase[cont]
     	cont += 1
   	return frase_nova