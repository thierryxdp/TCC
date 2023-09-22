def uppCons(frase):
    frasenova = frase[:]
    indice = 0
    while indice<len(frase):
        if frase[indice]!='a' and frase[indice]!='e' and frase[indice]!='i'
        and frase[indice]!='o' and frase[indice]!='u' and frase[indice]!='á'
        and frase[indice]!='ã' and frase[indice]!='à' and frase[indice]!='â'
        and frase[indice]!='é' and frase[indice]!='í' and frase[indice]!='ó'
        and frase[indice]!='ê' and frase[indice]!='ô' and frase[indice]!='õ'
        and frase[indice]!='ú':
        	consoante = str.upper(frase[indice])
            frasenova = str.replace(frasenova,frase[indice],consoante,1)
        indice = indice + 1
    return frasenova