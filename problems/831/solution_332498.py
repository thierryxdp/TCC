def lingua_p(palavra):
    i = 0
    frase2 = []
    while i < len(palavra):
        if palavra[i] in "aeiouAEIOUáâãéêíóôú":
            list.append(frase2, palavra[i] + 'p' + palavra[i])
        else:
            list.append(frase2, palavra[i])
        i = i + 1
    return str.join('',frase2)