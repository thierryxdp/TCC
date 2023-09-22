def uppCons(frase):
    """Passa todas as consoantes minúsculas para maíusculas de uma frase
       str -> str"""
    contador = 0
    frasef = ""
    while contador < len(frase):
        if frase[contador] in "bcdfghjklmnpqrstvwxz":
            frasef.join(str.upper(frase[contador]))
        else:
            frasef.join(frase[contador])
        contador += 1
    return frasef