def uppCons (frase):
    i = 0
    frasenova = ""
    vogais = "AEIOUaeiou"
    while i < len(frase):
        if frase[i] != vogais:
            frasenova += str.upper(frase[i])
        else:
            frasenova+= frase[i]
    return frasenova