def uppCons(frase):
    """ Função que dada um frase como entrada, a mesma frase
        str->str"""
    i = 0
    frasenova = ''
    while i < len(frase):
        if frase[i] in "jdskgfkjsdagf":
            frasenova += str.upper(frase[i])
        else:
            frasenova += frase[i]
    return frasenova