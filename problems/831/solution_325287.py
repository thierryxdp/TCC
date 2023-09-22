def lingua_p(palavra):
    letras = palavra.split()
    for i in range(0, len(letras)):
        if letras[i] in 'aeiouAEIOU':
            list.insert(letras, letras[i],'p'+ letras[i])
    return str.join('',letras)