def lingua_p(palavra):
    new = [n+'p'+n for n in palavra if n in 'aeiou']
    for n in palavra:
        if n in 'aeiou':
            n = n+'p'+n
        else:
            n = n
    return palavra