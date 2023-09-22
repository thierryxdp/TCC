def uppCons(frase):
    """Função que transforma as consoantes de uma frase em maiuscula; str->str """
    i=0
    frase2= ""
    while i < len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyzç":
            frase2+=frase[i].upper()
            

        else:
            frase2+=frase[i]

        i=i+1

    return frase2