def lingua_p(palavra):
    palavra = str.lower(palavra)
    for n in range(len(palavra)):
        if palavra[n] in 'aeiou':
            v = palavra[n]
            palavra = palavra.replace(v, str.upper(v+'p'+v)) 
    return string.lower(palavra)