def lingua_p(palavra):
    letras = list(palavra)
    i = 0
    while i < len(letras):
        if letras[i] in 'aeiouAEIOU':
            list.insert(letras, i+1, 'p' + letras[i])
        i = i + 1
    trad = str.join('', letras)
    return trad