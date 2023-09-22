def uppCons(frase):
    frasenova=""
    indice= 0
    while indice<len(frase):
        letra = frase[indice]
        if frase[indice] in "qwrtypsdfghjklçzxcvbnm":
            letra = str.upper(letra)
        frasenova = frasenova + letra
        indice = indice + 1
    return frasenova