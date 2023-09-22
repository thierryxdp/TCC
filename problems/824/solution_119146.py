def uppCons(frase):
    nova_frase = ""
    for x in frase:
        if x == "a" and "e" and "i" and "o" and "u":
            nova_frase = nova_frase + str.upper(x)
    return nova_frase