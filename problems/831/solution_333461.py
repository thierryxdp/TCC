def lingua_p(frase):
    """Dada uma funcao que receba como parametro uma palavra e retorne esta mesma
    palavra traduzida para lingua do P. Entrada: str,str-->str"""
    r = ""
    for z in x:
        if z in "aeiouéáú":
            r = r + z + "p" + z
        else:
            r = r + z
    return r