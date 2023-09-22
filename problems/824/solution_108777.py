def uppCons(frase):
    """Passa todas as consoantes minúsculas para maíusculas de uma frase
       str -> str"""
    contador = 0
    frasef = ""
    while contador < len(frase):
        caracter = frase[contador]
        if frase[contador] in "bcdfghjklmnpqrstvwxz":
            caracter = str.upper(frase[contador])
            frasef += caracter
        contador += 1
    return frasef