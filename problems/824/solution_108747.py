def uppCons (frase):
    i = 0
    frasenova = ""
    vogais = "AEIOUaeiou"
    while i < len(frase):
        if frase[i] != vogais:
            frasenova += str.upper(frase[i])
            i = i+1
        else:
            frasenova+= frase[i]
            i = i+1
    return frasenova