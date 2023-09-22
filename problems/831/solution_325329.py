def lingua_p(palavra):
    letras = list(palavra)
    for i in letras:
        if i in 'aeiouAEIOU':
            list.insert(letras, letras.index(i)+1, 'p' + i)
        i = i + 1
    trad = str.join('', letras)
    return trad