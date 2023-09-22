def uppCons (frase):
    i=0
    while i < len(frase):
        if frase[i] in 'aeiou':
            subir= str.upper (frase[i])
        i=i+1
    return subir