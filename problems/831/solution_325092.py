def lingua_p(palavra):
    palavra = palavra.lower()
    p = ''
    for i in palavra:
        p += i
        if i in "aeiouéíóúã":
            p += 'p' + i
    return p