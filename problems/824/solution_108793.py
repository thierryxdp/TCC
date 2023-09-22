def uppCons(frase):
    frasenova = frase[:]
    indice = 0
    while indice<len(frase):
        if frase[indice]!='a' and frase[indice]!='e' and frase[indice]!='i' and frase[indice]!='o' and frase[indice]!='u':
        	consoante = str.upper(frase[indice])
            frasenova = str.replace(frasenova,frase[indice],consoante,1)
        indice = indice + 1
    return frasenova