def uppCons (frase): 
    "Função que tem uma frase e retorne todas as consoantes da frase em maiúscula e os outros caracteres; str -> str"
    indice = 0
    frase2 = ''
    while indice < len(frase):
        if frase [indice] not in 'AaÁáàÃãÂâEeÉéÊêIiÍíOoÓóÕõÔôUuÚú':
            frase2 = frase2 + (str.upper(frase[indice]))