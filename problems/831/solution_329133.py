def lingua_p(palavra):
    new = [n+'p'+n for n in palavra if n in 'aeiou']
    return new