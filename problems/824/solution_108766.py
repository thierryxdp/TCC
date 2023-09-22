def uppCons(frase):
    """Passa todas as consoantes minúsculas para maíusculas de uma frase
       str -> str"""
    contador = 0
    frasef = ""
    while contador < len(frase):
        if frase[contador] in "bcdfghjklmnpqrstvwxz":
            str.join(frasef,str.upper(frase[contador]))
        str.join(frasef,frase[contador])
        contador += 1
    return frasef