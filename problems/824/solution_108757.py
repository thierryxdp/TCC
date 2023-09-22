def uppCons(frase):
    """Passa todas as consoantes minúsculas para maíusculas de uma frase
       str -> str"""
    contador = 0
    frasef = ""
    while contador < int(frase[0:]):
        if frase[contador] in "bcdfghjklmnpqrstvwxz":
            str.join(str.upper(frase[contador]),frasef)
        str.join(frase[contador],frasef)
        contador += 1
    return listaf