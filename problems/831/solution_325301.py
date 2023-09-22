def lingua_p(palavra):
    for i in range(0, len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            letras = str.split(palavra, palavra[i])
    return letras