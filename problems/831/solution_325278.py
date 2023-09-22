def lingua_p(palavra):
    letras = palavra.split()
    for i in range(0, len(letras)):
        if letras[i] in 'aeiouAEIOU':
            letras.insert('p'+ letras[i], letras[i])
    return letras.join()