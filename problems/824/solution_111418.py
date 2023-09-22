def uppCons(frase):
    contador = 0
    vogais = "aeiou"
    str.upper(frase)
    while contador < len(frase):
        if vogais in frase[contador]:
            str.replace(frase,frase[contador],str.lower(frase[contador])
     	contador = contador + 1
    return frase