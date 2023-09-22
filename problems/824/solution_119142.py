def uppCons(frase):
    nova_frase = ""
    for x in frase:
        if x != "a" or "e" or "i" or "o" or "u":
            str.append(nova_frase,str.upper(x))
    return nova_frase