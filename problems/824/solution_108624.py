def uppCons (frase): 
    indice = 0
    frase2 = ''
    while indice < len(frase):
        if frase [indice] not in 'AaÁáàÃãÂâEeÉéÊêIiÍíOoÓóÕõÔôUuÚú':
            frase2 = frase2 + (str.upper(frase[indice]))
        elif frase [indice] in 'AaÁáàÃãÂâEeÉéÊêIiÍíOoÓóÕõÔôUuÚú':
            frase2 = frase2 + frase [ indice ]
        indice = indice + 1 
    return frase2