def lingua_p(palavra):
    letras = list(palavra)
    for i in range:
        if letras[i] in 'aeiouAEIOU':
            list.insert(letras, i+1, 'p' + letras[i])
    if letras[-1] in 'aeiouAEIOU':
        list.append(letras, 'p'+letras[-1])
    trad = str.join('', letras)
    return trad