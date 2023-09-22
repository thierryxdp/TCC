def uppCons(frase):
    """Passa todas as consoantes minúsculas para maíusculas de uma frase
       str -> str"""
    contador = 0
    frasef = ""
    while contador < len(frase):
        if frase[contador] in "bcdfghjklmnpqrstvwxz":
            frase[contador] = str.upper(frase[contador])
        frasef += frase[contador]
        contador += 1
    return frasef