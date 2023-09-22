def lingua_p(frase):
    frase1=' '
    a=str.lower(frase)
    for i in a:
        frase1=frase1+i
        if i in 'aeiou':
            frase1=frase1+'p'+i
    return frase1