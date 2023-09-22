def lingua_p(palavra):
    palavra = palavra.lower()
    p = ''
    for i in palavra:
        p += i
        if i in "aeiouáéíóúã":
            p += 'p' + i
    return p