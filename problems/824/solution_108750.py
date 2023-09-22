def uppCons (frase):
    i = 0
    frasenova = ""
    vogais = "AEIOUÚÓÃÉúóãéaeiou"
    while i < len(frase):
        if frase[i] in vogais:
            frasenova += frase[i]
            i = i+1
        else:
            frasenova += str.upper(frase[i])
            i = i+1
    return frasenova