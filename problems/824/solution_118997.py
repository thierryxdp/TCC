def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
            frase = frase.replace(frase[contador], frase[contador].upper())
            contador += 1
            return frase