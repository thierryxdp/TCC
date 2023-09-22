def lingua_p(palavra):
    letras = list(palavra)
    for i in range(0, len(letras)):
        if letras[i] in 'aeiouAEIOU':
            list.insert(letras, i, letras[i] + 'p')
    trad = str.join('', letras)
    return trad