def uppCons(frase):
    nova_frase = ""
    for x in frase:
        if x != "a", "e", "i", "o", "u":
            nova_frase = nova_frase + str.upper(x)
        if x == "a", "e", "i", "o", "u":
            nova_frase = nova_frase + x
    return nova_frase