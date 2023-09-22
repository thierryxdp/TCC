def lingua_p(palavra):
    letras = list(palavra)
    for i in range(0, len(letras)):
        if letras[i] in 'aeiouAEIOU':
            letras = letras + list.insert(letras, i+1, 'p' + letras[i])
    trad = str.join('', letras)
    return trad