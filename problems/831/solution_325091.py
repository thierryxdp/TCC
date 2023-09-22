def lingua_p(palavra):
    palavra = palavra.lower()
    p = ''
    for i in palavra:
        p += i
        if i in "aeiouéíóú":
            p += 'p' + i
    return p