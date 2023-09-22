def uppCons (frase):
    i = 0
    frasenova = []
    vogais = "AEIOUaeiou"
    while i < len(frase):
        if frase[i] != vogais:
            str.upper(frase[i])
    return frasenova