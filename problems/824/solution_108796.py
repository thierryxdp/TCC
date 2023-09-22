def uppCons(frase):
    str.lower(frase)
    frase_upp=''
    l=0
    
    for letra in frase:
        if l!=['a' and 'e' and 'i' and 'o' and 'u' and 'á' and 'é' and 'í' and 'ó' and 'ú' and 'ê' and 'ô' and 'ã'):
               letra=str.upper(letra)
        l=l+1
        frase_upp=frase_upp+letra
    return frase_upp