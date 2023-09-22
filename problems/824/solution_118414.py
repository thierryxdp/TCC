uppCons(frase):
    frasenova=" "
    indice= 0
    while indice<len(frase):
        if frase[indice] in "qwrtypsdfghjklçzxcvbnm":
            str.upper(frase[indice])
        indice = indice + 1
    return frase