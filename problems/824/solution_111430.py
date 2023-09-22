def uppCons(frase):
    contador = 0
    vogais = ("AEIOU")
    d = str.upper(frase)
    while contador < len(frase):
        if d[contador] in vogais:
           d =str.replace(d,d[contador],str.lower(d[contador]))
        contador = contador + 1

    return d